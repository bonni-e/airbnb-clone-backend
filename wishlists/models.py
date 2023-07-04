from django.db import models
from common.models import CommonModel

# Create your models here.
class Wishlist(CommonModel) :
    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.Room",
        related_name="wishes"
        )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishes"
        )
    user = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE,
        related_name="wishes"
        )
    
