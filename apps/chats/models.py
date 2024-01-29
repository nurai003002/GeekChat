# models.py в приложении chats

from django.db import models
# from django.contrib.auth import get_user_model
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

class BackMessage(models.Model):
    username = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Соощение backend'
        verbose_name_plural = 'Сообщения backend'

class FrontMessage(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Соощение frontend'
        verbose_name_plural = 'Сообщения frontend'

class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        verbose_name = 'Соощение'
        verbose_name_plural = 'Сообщения'