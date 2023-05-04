# from django.urls import re_path
# from .consumers import ChatConsumer
#
# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
# ]

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>',ChatConsumer.as_asgi())
]
