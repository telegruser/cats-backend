import os

import requests
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Cat
from rest_framework import serializers


class CatsSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = ['id', 'name', 'birthday', 'breed', 'sex', 'datetime', 'owner']


# class LogInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         write_only_fields = ('password',)
#
#     def validate(self, attrs):
#         users = User.objects.filter(id=self.request)
#
#     def create(self, validated_data):
#         auth_server_url = os.environ.get('AUTH_SERVER_URL', 'http://127.0.0.1/o/token/')
#         request_body = {
#             'client_id': '1FeGEm1s6Tg1C5f5Yr9Ha4DVGqTAyyPi36pg9vYc',
#             'client_secret': 'sNwNEXOJ8OtQZpE7D9HYcQHTMHZMIIrteQxGmUgSBfvRiu5JIpgCzqi6YSIguh6jnjlEZHfgM8NE1QH4K9jDQh3yN'
#                              'Bn01TQ8mackZz4nDdKx4eDI9a7ceUn2ruUfqi1o',
#             'grant_type': 'password',
#             'username': validated_data['username'],
#         }
#         # requests.post(auth_server_url, '&'.join([f'{k}={v}' for k, v in request_body.items()]))
#         requests.post(auth_server_url, json=request_body)


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=True, write_only=True)
    # password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")  # , "password2")

    # def validate(self, attrs):
    #     if attrs["password1"] != attrs["password2"]:
    #         raise ValidationError({'password2': 'Не совпадают пароли'})
    #     return attrs

    def create(self, validated_data):
        # validated_data['password'] = validated_data.pop('password1')
        # validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
