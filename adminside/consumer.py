import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime


class AdminNotifications(AsyncWebsocketConsumer):
    async def connect(self):
        from .models import VendorNotification
        try:
            self.group_name = 'admin_group'
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            print('connected ')
            await self.accept()
        except Exception as e:
            print("Error in connect in admin notification", e)

    async def disconnect(self, close_code):
        try:
            print(f"Disconnected with code {close_code}")
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )
        except Exception as e:
            print("Error in disconnect admin notification:", e)

    async def receive(self, text_data):
        try:
            message = json.loads(text_data)
            print("admin_Received message:", message)
        except Exception as e:
            print("Error in receive admin notification:", e)

    async def create_notification(self, event):
        try:
            message = event['message']

            await self.send(json.dumps({

                'message': message,


            }))
        except Exception as e:
            print("Error in create admin notifications", e)
