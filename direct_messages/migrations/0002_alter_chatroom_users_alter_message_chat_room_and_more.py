# Generated by Django 4.2.2 on 2023-07-04 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('direct_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='chat_rooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='direct_messages.chatroom'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
