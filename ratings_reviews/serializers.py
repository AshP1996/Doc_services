from rest_framework import serializers
from .models import Rating, Review

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'doctor', 'rating', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'doctor', 'review', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
