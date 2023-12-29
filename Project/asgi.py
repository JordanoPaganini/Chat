import os
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PI24.settings')

django_asgi_http = get_asgi_application()

from websockets import routing

application = ProtocolTypeRouter({
    "http": django_asgi_http,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(routing.websocket_urlpatterns)
        )
    )
})

ASGI_APPLICATION = application