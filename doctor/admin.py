from django.contrib import admin
from .models import DoctorProfile, Service, ProfileEntity

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'experience', 'phone_number', 'fees')
    search_fields = ('name', 'top_expertise', 'city', 'hospital')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)
    search_fields = ('service_name',)

@admin.register(ProfileEntity)
class ProfileEntityAdmin(admin.ModelAdmin):
    list_display = ('entity_type', 'entity_value')
    search_fields = ('entity_type',)
