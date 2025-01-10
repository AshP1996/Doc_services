from rest_framework import serializers
from .models import DoctorProfile, Service, ProfileEntity

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name']

class ProfileEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileEntity
        fields = ['id', 'entity_type', 'entity_value']

class DoctorProfileSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, required=False)
    entities = ProfileEntitySerializer(many=True, required=False)

    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def validate_phone_number(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def validate_fees(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Fees must be a positive number.")
        return value

    def create(self, validated_data):
        services_data = validated_data.pop('services', [])
        entities_data = validated_data.pop('entities', [])
        doctor_profile = DoctorProfile.objects.create(**validated_data)
        
        for service_data in services_data:
            Service.objects.create(doctor=doctor_profile, **service_data)
        for entity_data in entities_data:
            ProfileEntity.objects.create(doctor=doctor_profile, **entity_data)
        
        return doctor_profile

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services', [])
        entities_data = validated_data.pop('entities', [])

        instance = super().update(instance, validated_data)
        instance.services.all().delete()
        instance.entities.all().delete()
        
        for service_data in services_data:
            Service.objects.create(doctor=instance, **service_data)
        for entity_data in entities_data:
            ProfileEntity.objects.create(doctor=instance, **entity_data)
        
        return instance
