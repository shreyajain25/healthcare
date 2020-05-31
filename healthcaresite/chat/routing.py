from channels import route
from dashboard import consumers

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]

channel_routing = [
    route('websocket.connect', consumers.ws_connect),
    route('websocket.recieve', consumers.ws_receive),
    route('websocket.disconnect', consumers.ws_disconnect),
]

routing_chat = [
    route('chat.receive', consumers.ws_join, command='^join$'),
    route('chat.receive', consumers.ws_leave, command='^leave$'),
    route('chat.receive', consumers.ws_send, command='^send$'),
]
