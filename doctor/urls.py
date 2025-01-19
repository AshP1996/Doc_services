from django.urls import path
from .views import DoctorProfileListCreateView, DoctorProfileDetailView

urlpatterns = [
    path('docto r-profiles/', DoctorProfileListCreateView.as_view(), name='doctor-profile-list-create'),
    path('doctor-profiles/<int:pk>/', DoctorProfileDetailView.as_view(), name='doctor-profile-detail'),
]
