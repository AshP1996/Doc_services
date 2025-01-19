from django.db import models
from django.conf import settings
from doctor.models import DoctorProfile

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()  # Assuming rating is from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'doctor')  # Prevent multiple ratings from the same user for the same doctor

    def __str__(self):
        return f"Rating: {self.rating} by {self.user.email} for Dr. {self.doctor.name}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'doctor')  # Prevent multiple reviews from the same user for the same doctor

    def __str__(self):
        return f"Review by {self.user.email} for Dr. {self.doctor.name}"
