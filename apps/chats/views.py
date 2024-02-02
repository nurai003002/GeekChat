from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Message,Rooms
from .serializers import RoomSerializer,BackMessageSerializer,FrontMessageSerializer,UXUIMessageSerializer,AndroidMessageSerializer

class BackListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = BackMessageSerializer

class RoomsListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

# class FrontListViewSet(GenericViewSet,
#                       mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset = Message.objects.all()
#     serializer_class = FrontMessageSerializer

# class UxUiListViewSet(GenericViewSet,
#                       mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset = Message.objects.all()
#     serializer_class = UXUIMessageSerializer

# class AndroidListViewSet(GenericViewSet,
#                       mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset = Message.objects.all()
#     serializer_class = AndroidMessageSerializer


# views.py
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render,redirect

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
