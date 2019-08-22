from django.db import models

# Create your models here.
# from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers


class Cat(models.Model):
    SEX_CHOICES = ('m', 'мужской'), ('w', 'женский')
    name = models.TextField(verbose_name='Имя')
    birthday = models.DateField(verbose_name='День рождения')
    breed = models.CharField(max_length=30, verbose_name='Порода')
    sex = models.CharField(max_length=1, verbose_name='Пол', choices=SEX_CHOICES)  # m/f
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, null=False)
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    datetime = models.DateTimeField(verbose_name='Добавлен', auto_now_add=True)


# class User(models.Model):

