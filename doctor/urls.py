from django.urls import path
from .views import DoctorProfileListCreateView, DoctorProfileDetailView, PublicDoctorProfileDetailView, AllDoctorProfilesView

urlpatterns = [
    path('doctor-profiles/', DoctorProfileListCreateView.as_view(), name='doctor-profile-list-create'),
    path('doctor-profiles/<int:pk>/', DoctorProfileDetailView.as_view(), name='doctor-profile-detail'),
    path('public-doctor-profiles/<int:pk>/', PublicDoctorProfileDetailView.as_view(), name='public-doctor-profile-detail'),
    path('all-doctor-profiles/', AllDoctorProfilesView.as_view(), name='all-doctor-profiles'),
]
