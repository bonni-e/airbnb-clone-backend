from django.db import models
from common.models import CommonModel

# Create your models here.
class ChatRoom(CommonModel) :
    users = models.ManyToManyField("users.User")

    def __str__(self) -> str:
        return "Chatting room"

class Message(CommonModel) :
    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    chat_room = models.ForeignKey("direct_messages.ChatRoom", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} says : {self.text}"