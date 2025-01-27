from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/accounts/', include('accounts.urls')),  # Include URLs from accounts app
    path('api/doctor/', include('doctor.urls')),  # Include URLs from doctor app
    path('api/dashboard/', include('dashboard.urls')), 
    path('api/chat/', include('chat.urls')),
    path('api/rating_reviews/', include('ratings_reviews.urls')),
]
