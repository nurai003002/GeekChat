from rest_framework import serializers
from .models import Rooms,ChatMessage

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class ChatMessageserializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
