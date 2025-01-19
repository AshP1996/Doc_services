from django.contrib import admin
from .models import Rating, Review

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'rating', 'created_at')
    search_fields = ('user__email', 'doctor__name')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'review', 'created_at')
    search_fields = ('user__email', 'doctor__name', 'review')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
