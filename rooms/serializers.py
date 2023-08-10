from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializer import TinyUserSerializer
from categories.serializers import CategorySerializer

class AmenitySerializer(ModelSerializer) :
    class Meta : 
        model = Amenity
        fields = "__all__"

class RoomSerializer(ModelSerializer) :
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    def create(self, validated_data):
        print("validated_data : ", validated_data)
        return super().create(validated_data)

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
