from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializer import TinyUserSerializer

class AmenitySerializer(ModelSerializer) :
    class Meta : 
        model = Amenity
        fields = "__all__"

class RoomSerializer(ModelSerializer) :
    owner = TinyUserSerializer(read_only=True)

    class Meta : 
        model = Room 
        fields = "__all__"
        # depth = 1

class RoomListSerializer(ModelSerializer) :
    class Meta : 
        model = Room 
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        );
