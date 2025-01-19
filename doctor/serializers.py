from rest_framework import serializers
from .models import DoctorProfile, Service, ProfileEntity
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name']

class ProfileEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileEntity
        fields = ['id', 'entity_type', 'entity_value']

class DoctorProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    services = ServiceSerializer(many=True, required=False)
    entities = ProfileEntitySerializer(many=True, required=False)

    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def create(self, validated_data):
        services_data = validated_data.pop('services', [])
        entities_data = validated_data.pop('entities', [])
        user = self.context['request'].user
        doctor_profile = DoctorProfile.objects.create(user=user, **validated_data)
        
        for service_data in services_data:
            Service.objects.create(doctor=doctor_profile, **service_data)
        for entity_data in entities_data:
            ProfileEntity.objects.create(doctor=doctor_profile, **entity_data)
        
        return doctor_profile

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services', [])
        entities_data = validated_data.pop('entities', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        instance.services.all().delete()
        instance.entities.all().delete()
        
        for service_data in services_data:
            Service.objects.create(doctor=instance, **service_data)
        for entity_data in entities_data:
            ProfileEntity.objects.create(doctor=instance, **entity_data)
        
        return instance
