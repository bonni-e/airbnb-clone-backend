from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
# def reset_prices(model_admin, request, queryset) :
def reset_prices(model_admin, request, rooms) :
    print(model_admin)
    print(dir(request))
    print(rooms)

    for room in rooms.all() :
        room.price = 0
        room.save()
        
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin) :

    # 액션을 만들어 추가할 수 있음 
    actions = (
        reset_prices,
    )

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",  # 아래 메소드의 결과값 
        "rating",
        "owner",
        "created_at",
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

    search_fields = (
        "name",
        # "price",              # __contains 로 기본 검색을 함 (0 검색 시, 0을 포함하는 키워드를 확인하면 조회가 됨)
        # "^price"              # __startswith 로 검색을 하도록 ^을 붙여줌 
        "=price",               # 정확히 일치하는 값 확인 

        "^owner__username",     # 직접 orm 함수를 사용할 수도 있음 
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