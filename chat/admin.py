from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'created_at')
    search_fields = ('user__email', 'doctor__email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    autocomplete_fields = ('user', 'doctor')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_room', 'sender', 'timestamp', 'short_content')
    search_fields = (
        'sender__email',
        'chat_room__user__email',
        'chat_room__doctor__email',
        'content',
    )
    list_filter = ('timestamp', 'chat_room')
    ordering = ('-timestamp',)
    autocomplete_fields = ('chat_room', 'sender')

    @staticmethod
    def short_content(obj):
        """Display a truncated version of the message content."""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = 'Content'
