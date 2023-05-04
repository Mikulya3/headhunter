import json
from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from .models import Chat
from ..userprofile.models import UserProfile

User = get_user_model()

class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self): # подключение
        print("Websocket connect!")
        await database_sync_to_async(self.get_user)()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def receive_json(self, content, **kwargs):
        if content['msg'] != None:
            await database_sync_to_async(save_to_database)(self, content)
            await self.channel_layer.group_send(self.room_name,
                                                {
                                                    'type': 'chat.message',
                                                    'msg': content['msg']
                                                })

    async def disconnect(self, close_code): # отключение
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        self.close()
        raise StopConsumer()

    async def chat_message(self, event):
        msg = json.dumps({'msg': event['msg']})
        await self.send(msg)

    def get_user(self): # вытаскиваем юзера
        session_key = 'zdpagvtfetm7h4gsk996c5tl8ecmoc11'
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        print('User obtained through session key', user)
        return user


# Outside the consumer class
def save_to_database(self, content): # сохранение в базу данных
    group = Chat.objects.get(name=self.room_name)
    profile = UserProfile.objects.get(user=self.user)
    chat = Chat.objects.create(message=content['msg'], group=group, send_by=profile)
    chat.save()
