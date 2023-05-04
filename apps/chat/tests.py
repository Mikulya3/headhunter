import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.chat.consumers import ChatConsumer
from django.test import TestCase
from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async
from apps.chat.models import Chat
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import get_user_model

User = get_user_model()
class ChatConsumerTestCase(TestCase):
    async def get_user(self):
        # create a session for the user
        session = SessionStore()
        session['_auth_user_id'] = self.user.id
        session.save()
        # get the user from the session
        self.scope['session'] = session
        return self.user

    async def test_chat_consumer(self):
        # Create a user for the test
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass'
        )

        self.room_name = 'testroom'

    async def tearDown(self):
        self.websocket.disconnect()
        self.websocket = None
        self.async_db.close()

        communicator = WebsocketCommunicator(
            ChatConsumer.as_asgi(),
            f'/ws/chat/{self.room_name}/'
        )

        # подключение в сокетам
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # отправка сообщения сокетам
        message = 'Hello, world!'
        await communicator.send_json_to({'msg': message})

        # проверка на сораняемость сообщений и тд
        saved_chat = await database_sync_to_async(Chat.objects.last)()
        self.assertEqual(saved_chat.message, message)
        self.assertEqual(saved_chat.group.name, self.room_name)


        # отсоединение от сокета
        await communicator.disconnect()
        self.assertFalse(communicator.is_connected)
