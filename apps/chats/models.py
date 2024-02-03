# models.py в приложении chats

from django.db import models
from apps.users.models import User
class Rooms(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    topic = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='Комната'
        verbose_name_plural = 'Комнаты'

from django.db import models

class ChatMessage(models.Model):
    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Соощение'
        verbose_name_plural = 'Сообщения'