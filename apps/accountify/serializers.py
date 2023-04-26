from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accountify.tasks import send_confirmation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=5, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email(user.email, code)
        return user