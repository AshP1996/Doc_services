# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from accounts.models import CustomUser
# from doctor.models import DoctorProfile
# # from appointments.models import Appointment
# # from chat.models import Message
# # from notifications.models import Notification
# from .serializers import DashboardSerializer, DoctorDashboardSerializer

# class UserDashboardView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         data = {}
        
#         if user.user_type == 'doctor':
#             profile = DoctorProfile.objects.get(user=user)
#             # appointments = Appointment.objects.filter(doctor=user)
#             # messages = Message.objects.filter(receiver=user)
#             # notifications = Notification.objects.filter(user=user)
#             data = {
#                 "profile": DoctorDashboardSerializer(profile).data,
#                 # "appointments": appointments.values(),
#                 # "messages": messages.values(),
#                 # "notifications": notifications.values()
#             }
#         else:  # user_type == 'user'
#             profile = CustomUser.objects.get(id=user.id)
#             # appointments = Appointment.objects.filter(user=user)
#             # messages = Message.objects.filter(receiver=user)
#             # notifications = Notification.objects.filter(user=user)
#             data = {
#                 "profile": DashboardSerializer(profile).data,
#                 # "appointments": appointments.values(),
#                 # "messages": messages.values(),
#                 # "notifications": notifications.values()
#             }
#         return Response(data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from doctor.models import DoctorProfile
from .serializers import DashboardSerializer, DoctorDashboardSerializer

class DoctorDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.user_type != 'doctor':
            return Response({"error": "You are not authorized to access this page."}, status=403)

        profile = DoctorProfile.objects.get(user=user)
        # Optional: Fetch related data such as appointments, messages, etc.
        data = {
            "profile": DoctorDashboardSerializer(profile).data,
            # Add more fields as needed, e.g., "appointments", "messages", etc.
        }
        return Response(data)

class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.user_type != 'user':
            return Response({"error": "You are not authorized to access this page."}, status=403)

        profile = CustomUser.objects.get(id=user.id)
        data = {
            "profile": DashboardSerializer(profile).data,
            # Add more fields if needed, e.g., appointments, messages, etc.
        }
        return Response(data)
