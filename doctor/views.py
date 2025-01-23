from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser

class DoctorProfileListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profiles = DoctorProfile.objects.filter(user=request.user)
        serializer = DoctorProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorProfileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        print("profile for get", profile)
        serializer = DoctorProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        print("profile for put", profile)

        serializer = DoctorProfileSerializer(profile, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        profile.delete()
        return Response({"detail": "Doctor profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class PublicDoctorProfileDetailView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication required

    def get(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk)
        serializer = DoctorProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllDoctorProfilesView(APIView):
    permission_classes = [permissions.AllowAny]  # Public access

    def get(self, request):
        # Get all users with user_type 'doctor'
        doctor_users = CustomUser.objects.filter(user_type="doctor").values_list('id', flat=True)
        # Get doctor profiles linked to these users
        profiles = DoctorProfile.objects.filter(user_id__in=doctor_users)
        serializer = DoctorProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)