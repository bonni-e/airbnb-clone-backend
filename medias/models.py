from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel) :
    file = models.ImageField()
    description = models.TextField()
    room = models.ForeignKey(
        "rooms.Room", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="photos"
        )
    experience = models.ForeignKey(
        "experiences.Experience", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="photos"
        )

    def __str__(self) -> str:
        return "Photo File"

class Video(CommonModel) :
    file = models.FileField()
    description = models.TextField()
    experience = models.OneToOneField(
        "experiences.Experience", 
        on_delete=models.CASCADE, 
        related_name="video"
        ) 
    # OneToOneField : Unique 하나의 활동에 대하여 하나의 동영상만 허용 

    def __str__(self) -> str:
        return "Video File" 