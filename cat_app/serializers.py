from rest_framework import serializers
from .models import Cat


class CatsSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = ['id', 'name', 'birthday', 'breed', 'sex', 'datetime']
