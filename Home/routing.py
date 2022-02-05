from django.urls import path
from .consumers import MyConsumer




ws_patterns=[
    path('ws/test/<booth_id>',MyConsumer.as_asgi())
]
