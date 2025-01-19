from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer
from django.shortcuts import get_object_or_404

class DoctorProfileListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profiles = DoctorProfile.objects.filter(user=request.user)
        serializer = DoctorProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorProfileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        serializer = DoctorProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        serializer = DoctorProfileSerializer(profile, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = get_object_or_404(DoctorProfile, pk=pk, user=request.user)
        profile.delete()
        return Response({"detail": "Doctor profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
