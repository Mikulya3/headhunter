#
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()
#
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import apps.chat.routing
#
# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             apps.chat.routing.websocket_urlpatterns
#         )
#     ),
# })

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.chat.consumers import ChatConsumer

django_asgi_app = get_asgi_application()

def websocket_application(scope):
    return AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/chat/<str:room_name>', ChatConsumer.as_asgi())
            ])
        )
    )(scope)

application = ProtocolTypeRouter({

    "http": django_asgi_app,
    "websocket": websocket_application,

})




