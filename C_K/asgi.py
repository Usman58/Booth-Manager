# mysite/asgi.py
import os
from channels.auth import AuthMiddlewareStack
from Home.routing import ws_patterns

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE','C_K.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(ws_patterns)),
})
