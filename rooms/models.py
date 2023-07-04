from django.db import models
from common.models import CommonModel

# Create your models here.
# class Romm(models.Model) :
class Room(CommonModel) :   # 만들어둔 모델을 상속 받아 공통 필드를 가짐
    class RoomKindChoices(models.TextChoices) :
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=False)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True)

    # 외래키 설정 (N:1)
    # ㄴ room1, room2, room3 -> owner1 
    owner = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE,
        related_name="rooms"        # _set 커스터마이징함 
        )

    # 편의 시설 (N:M 관계 설정)
    # ㄴ room1, room2, room3 모두 -> amenity1, amenity2, amenity3 을 가질 수 있음  
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms"
        )

    # 모든 모델들이 다음 필드값을 공통으로 갖도록 -> common 앱을 생성 후, CommonModel 작성 -> 상속 받기 
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def total_amenities(self) :
        # return self.amenities.count()
        return self.amenities.filter().exclude().count()


# class Amenity(models.Model) :
class Amenity(CommonModel) :
    """ Amenity Definition """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"