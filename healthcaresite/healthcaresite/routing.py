# from channels.routing import ProtocolTypeRouter
from channels import include
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
# application = ProtocolTypeRouter({
# Empty for now (http->django views is added by default)
# })

# application = [
#     # To set up the websocket routing
#     include('chat.routing.channel_routing', path=r'^ /socket /'),
#     # For chat join, leave, and send
#     include('chat.routing.routing_chat'),
# ]
