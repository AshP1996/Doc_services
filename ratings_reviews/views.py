from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Rating, Review
from .serializers import RatingSerializer, ReviewSerializer
from doctor.models import DoctorProfile

class RatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            doctor_id = request.data.get('doctor')
            try:
                doctor = DoctorProfile.objects.get(id=doctor_id)
            except DoctorProfile.DoesNotExist:
                return Response({"error": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer.save(user=request.user, doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        doctor_id = request.query_params.get('doctor')
        if not doctor_id:
            return Response({"error": "Doctor ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            doctor = DoctorProfile.objects.get(id=doctor_id)
        except DoctorProfile.DoesNotExist:
            return Response({"error": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)

        ratings = Rating.objects.filter(doctor=doctor)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

class ReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            doctor_id = request.data.get('doctor')
            try:
                doctor = DoctorProfile.objects.get(id=doctor_id)
            except DoctorProfile.DoesNotExist:
                return Response({"error": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer.save(user=request.user, doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        doctor_id = request.query_params.get('doctor')
        if not doctor_id:
            return Response({"error": "Doctor ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            doctor = DoctorProfile.objects.get(id=doctor_id)
        except DoctorProfile.DoesNotExist:
            return Response({"error": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)

        reviews = Review.objects.filter(doctor=doctor)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
