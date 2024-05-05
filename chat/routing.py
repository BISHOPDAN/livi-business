from django.urls import path
from .consumers import ChatConsumer
from adminside.consumer import AdminNotifications
# NotificationConsumer


websocket_urlpatterns = [
    path('ws/chat/<int:id>/', ChatConsumer.as_asgi()),
    path('ws/admin-notifications/', AdminNotifications.as_asgi()),
    # path("ws/notifications/<int:user_id>/", NotificationConsumer.as_asgi()),
]
