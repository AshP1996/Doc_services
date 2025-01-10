from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from doctor.models import DoctorProfile
# from appointments.models import Appointment
# from chat.models import Message
# from notifications.models import Notification
from .serializers import DashboardSerializer, DoctorDashboardSerializer

class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {}
        
        if user.user_type == 'doctor':
            profile = DoctorProfile.objects.get(user=user)
            # appointments = Appointment.objects.filter(doctor=user)
            # messages = Message.objects.filter(receiver=user)
            # notifications = Notification.objects.filter(user=user)
            data = {
                "profile": DoctorDashboardSerializer(profile).data,
                # "appointments": appointments.values(),
                # "messages": messages.values(),
                # "notifications": notifications.values()
            }
        else:  # user_type == 'user'
            profile = CustomUser.objects.get(id=user.id)
            # appointments = Appointment.objects.filter(user=user)
            # messages = Message.objects.filter(receiver=user)
            # notifications = Notification.objects.filter(user=user)
            data = {
                "profile": DashboardSerializer(profile).data,
                # "appointments": appointments.values(),
                # "messages": messages.values(),
                # "notifications": notifications.values()
            }
        return Response(data)
