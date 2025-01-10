from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'created_at')
    search_fields = ('user__email', 'doctor__email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_room', 'sender', 'timestamp', 'content')
    search_fields = ('sender__email', 'chat_room__user__email', 'chat_room__doctor__email', 'content')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
