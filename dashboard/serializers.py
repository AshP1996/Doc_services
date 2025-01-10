from rest_framework import serializers
from accounts.models import CustomUser
from doctor.models import DoctorProfile

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'firstname', 'lastname', 'user_type']

class DoctorDashboardSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField(many=True)
    entities = serializers.StringRelatedField(many=True)

    class Meta:
        model = DoctorProfile
        fields = [
            'user',
            'name',
            'degree',
            'experience',
            'top_expertise',
            'phone_number',
            'description',
            'page_url',
            'area',
            'city',
            'address',
            'hospital',
            'fees',
            'available_days',
            'available_timings',
            'latitude',
            'longitude',
            'services',
            'entities',
        ]

# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = '__all__'

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'
