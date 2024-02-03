from django.contrib import admin

from apps.chats.models import  Rooms,ChatMessage
# Register your models here.


@admin.register(Rooms)
class RoomBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic')
    list_filter = ('name', 'topic')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'sender', 'content', 'timestamp')
    search_fields = ('room_name__name', 'sender', 'content') 
    


