from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


from asgiref.sync import sync_to_async

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # code here to create user object
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # replace user.save() with sync_to_async(user.save) below
        sync_to_async(user.save, thread_sensitive=True)()
        return user
