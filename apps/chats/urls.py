# from rest_framework.routers import DefaultRouter
# # from django.urls import path

# from apps.chats.views import BackListViewSet,FrontListViewSet,UxUiListViewSet,AndroidListViewSet,RoomsListViewSet

# router = DefaultRouter()

# router.register('backend', BackListViewSet, basename='api_chats_backend')
# router.register('frontend', FrontListViewSet, basename='api_chats_frontend')
# router.register('UxUi', UxUiListViewSet, basename='api_chats_UxUi')
# router.register('android', AndroidListViewSet, basename='api_chats_android')
# router.register('rooms', RoomsListViewSet, basename='api_chats_rooms')

# urlpatterns = router.urls

# apps/chats/urls.py
# views.py
# chats/urls.py
from django.urls import path
from .views import ChatRoomView

app_name = 'chats'

urlpatterns = [
    path('room/<str:room_name>/', ChatRoomView.as_view(), name='chat_room'),
    # Другие URL-пути вашего приложения
]
