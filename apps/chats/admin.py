from django.contrib import admin

from apps.chats.models import Message, Rooms,BackMessage,FrontMessage
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('username','content', 
                    'timestamp',)
    list_filter = ('username', 'content', 
                    'timestamp',)


@admin.register(Rooms)
class RoomBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic')
    list_filter = ('name', 'topic')

    


