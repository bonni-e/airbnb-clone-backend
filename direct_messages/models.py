from django.db import models
from common.models import CommonModel

# Create your models here.
class ChatRoom(CommonModel) :
    users = models.ManyToManyField(
        "users.User",
        related_name="chat_rooms"
        )

    def __str__(self) -> str:
        return "Chatting room"

class Message(CommonModel) :
    text = models.TextField()
    user = models.ForeignKey(
        "users.User", 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="messages"
        )
    chat_room = models.ForeignKey(
        "direct_messages.ChatRoom", 
        on_delete=models.CASCADE,
        related_name="messages"
        )

    def __str__(self) -> str:
        return f"{self.user} says : {self.text}"