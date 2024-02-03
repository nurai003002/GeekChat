from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from apps.chats.models import ChatMessage,Rooms
from .serializers import RoomSerializer, ChatMessageserializer


class RoomsListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

class ChatMessageView(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageserializer

    def save_chat_message(room_name, sender, content):
        message = ChatMessage(room_name=room_name, sender=sender, content=content)
        message.save()

class ChatRoomView(TemplateView):
    template_name = 'chat_room.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['room_name'] = self.kwargs['room_name']
        return context
    def post(self, request, *args, **kwargs):
        create_topic = request.POST.get('create_topic', '')

        response_data = {'status': 'success', 'create_topic': create_topic}
        return JsonResponse(response_data)

        

class CreateTopicView(View):
    template_name = 'create_topic.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        create_topic = request.POST.get('create_topic', '')

        response_data = {'status': 'success', 'create_topic': create_topic}
        return JsonResponse(response_data)


    

