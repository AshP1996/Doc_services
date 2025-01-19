from django.urls import path
from .views import UserDashboardView, DoctorDashboardView

urlpatterns = [
    path('dashboard/user/', UserDashboardView.as_view(), name='user-dashboard'),
    path('dashboard/doctor/', DoctorDashboardView.as_view(), name='doctor-dashboard'),
]
