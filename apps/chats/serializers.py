from rest_framework import serializers
from .models import Message, Message,Rooms,BackMessage

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class BackMessageSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='username.user.username', read_only=True)  # Обратите внимание на изменение source

    class Meta:
        model = BackMessage  # Исправлено на BackMessage
        fields = ('username', 'content', 'timestamp')
        

class FrontMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ( 'username', 'content', 'timestamp')

class UXUIMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields =( 'username', 'content', 'timestamp')

class AndroidMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ( 'username', 'content', 'timestamp')

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ( 'username', 'content', 'timestamp')