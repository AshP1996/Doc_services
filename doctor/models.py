from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    profile_pic = models.ImageField(upload_to='doctor_profiles/', null=True, blank=True)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    top_expertise = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    page_url = models.URLField(null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    hospital = models.CharField(max_length=255, null=True, blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_days = models.CharField(max_length=255, null=True, blank=True)
    available_timings = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.degree}"

class Service(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name

class ProfileEntity(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='entities')
    entity_type = models.CharField(max_length=50)
    entity_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.entity_type}: {self.entity_value}"
