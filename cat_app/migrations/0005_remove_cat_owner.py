# Generated by Django 2.2.4 on 2019-08-19 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0004_auto_20190819_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='owner',
        ),
    ]
