from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin) :
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",  # 아래 메소드의 결과값 
        "owner",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )

    # admin 에 메소드를 주거나, model 에서 정의하면 됨 
    # def total_amenities(self, room) :
    #     return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin) :
    list_display = (
        "name",
        "description",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "created_at",
        "modified_at",
    )