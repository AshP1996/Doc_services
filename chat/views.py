from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from accounts.models import CustomUser

class ChatRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chat_rooms = ChatRoom.objects.filter(user=request.user) | ChatRoom.objects.filter(doctor=request.user)
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        doctor_id = request.data.get('doctor_id')
        doctor = CustomUser.objects.get(id=doctor_id)
        if doctor.user_type != 'doctor':
            return Response({"error": "Invalid doctor ID."}, status=status.HTTP_400_BAD_REQUEST)

        chat_room, created = ChatRoom.objects.get_or_create(user=user, doctor=doctor)
        serializer = ChatRoomSerializer(chat_room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, chat_room_id):
        messages = Message.objects.filter(chat_room_id=chat_room_id).order_by('timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, chat_room_id):
        chat_room = ChatRoom.objects.get(id=chat_room_id)
        content = request.data.get('content')
        message = Message.objects.create(chat_room=chat_room, sender=request.user, content=content)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
