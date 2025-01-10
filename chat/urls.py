from django.urls import path
from .views import ChatRoomView, MessageView

urlpatterns = [
    path('chatrooms/', ChatRoomView.as_view(), name='chat-room-list'),
    path('chatrooms/<int:chat_room_id>/messages/', MessageView.as_view(), name='message-list-create'),
]
