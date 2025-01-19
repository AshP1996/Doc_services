from django.contrib.auth.models import update_last_login
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ResetPasswordRequestSerializer,
    ResetPasswordConfirmSerializer,
)
from .models import CustomUser as User
import logging

logger = logging.getLogger(__name__)

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'user_type': user.user_type,
            }
        })


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"
            
            # Log the reset request
            logger.info(f"Password reset requested for email: {email}")

            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )

        return Response(
            {'message': 'If an account with that email exists, a reset link has been sent.'},
            status=status.HTTP_200_OK
        )


class ResetPasswordConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uid = force_str(urlsafe_base64_decode(serializer.validated_data['uid']))
        user = User.objects.get(pk=uid)
        token = serializer.validated_data['token']

        if PasswordResetTokenGenerator().check_token(user, token):
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
