from django.urls import path
from .views import (
    SignupView,
    LoginView,
    LogoutView,
    ResetPasswordRequestView,
    ResetPasswordConfirmView,
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', ResetPasswordRequestView.as_view(), name='password_reset_request'),
    path('reset_password_confirm/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
]
