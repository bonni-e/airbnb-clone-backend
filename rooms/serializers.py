from rest_framework import serializers
from .models import *
from users.serializer import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import *
from wishlists.models import Wishlist

class AmenitySerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Amenity
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer) :
    owner = TinyUserSerializer(read_only=True)
    # amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(read_only=True, many=True)

    '''
    * custom field 
    '''
    rating =  serializers.SerializerMethodField(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)

    # 역접근자 활용 (권장하지 않음 -> Pagenation)
    # reviews = ReviewSerializer(many=True, read_only=True)

    def get_rating(self, room) :
        return room.rating()
    
    # 방을 조회하는 유저에 따라 값이 달라지는 '동적 필드'
    def get_is_owner(self, room) :
        return room.owner == self.context["request"].user

    def create(self, validated_data):
        print("validated_data : ", validated_data)
        return super().create(validated_data)
    '''
    '''

    class Meta : 
        model = Room 
        exclude = ['amenities']
        # fields = "__all__"
        # depth = 1

class RoomListSerializer(serializers.ModelSerializer) :
    rating = serializers.SerializerMethodField(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)
    photos = PhotoSerializer(read_only=True, many=True)

    def get_rating(self, room) :
        return room.rating()
    
    def get_is_owner(self, room) :
        request = self.context["request"]
        if request:
            return room.owner == request.user
        return False
    
    def get_is_liked(self, room) :
        request = self.context['request']
        return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()

        # wishlists = Wishlist.objects.filter(user=request.user)

        # if request :
        #     for wishlist in wishlists :
        #         try :
        #             room = wishlist.rooms.get(pk=room.pk)
        #             if room :
        #                 return True
        #         except :
        #             pass
        # return False

    class Meta : 
        model = Room 
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "is_liked",
            "photos",
        );