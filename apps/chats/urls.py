from rest_framework.routers import DefaultRouter
# from django.urls import path

from apps.chats.views import RoomsListViewSet,ChatMessageView
router = DefaultRouter()

router.register('rooms', RoomsListViewSet, basename='api_chats_rooms')
router.register('message', ChatMessageView, basename='api_chats_message')


from django.urls import path
from .views import ChatRoomView,CreateTopicView

app_name = 'chats'

urlpatterns = [
    path('room/<str:room_name>/', ChatRoomView.as_view(), name='chat_room'),
    path('create_topic/', CreateTopicView.as_view(), name='create_topic'),
]
urlpatterns += router.urls
