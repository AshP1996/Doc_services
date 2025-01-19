from django.urls import path
from .views import RatingView, ReviewView

urlpatterns = [
    path('ratings/', RatingView.as_view(), name='ratings'),
    path('reviews/', ReviewView.as_view(), name='reviews'),
]
