from django.contrib.auth.models import User

from .models import Cat
from rest_framework import serializers


class CatsSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = ['id', 'name', 'birthday', 'breed', 'sex', 'datetime', 'owner']


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
