from rest_framework import serializers
from .models import ChatRoom, Message
from accounts.models import CustomUser

class ChatRoomSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'user', 'doctor', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id', 'chat_room', 'sender', 'content', 'timestamp']
