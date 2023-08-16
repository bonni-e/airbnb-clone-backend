from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import status
from .models import Wishlist
from rooms.models import Room
from .serializers import WishlistSerializer
from rooms.serializers import RoomSerializer

class Wishlists(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(all_wishlists, many=True, context={"request" : request})
        return Response(serializer.data)

    def post(self, request) :
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid() :
            try :
                room = Room.objects.get(name=request.data.get("name"))
            except Room.DoesNotExist :
                raise exceptions.NotFound
            
            serializer.save(user=request.user)
        else :
            raise Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)
        

class WishlistDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user) :
        try :
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist :
            raise exceptions.NotFound

    def get(self, request, pk) :
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(wishlist, context={"request" : request})
        return Response(serializer.data)

    def put(self, request, pk) :
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(instance=wishlist, data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)

    def delete(self, request, pk) :
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    

class WishlistRooms(APIView) :
    permission_classes = [IsAuthenticated]

    def get_list(self, pk) :
        try :
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist :
            raise exceptions.NotFound
        
    def get_room(self, pk) :
        try :
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist :
            raise exceptions.NotFound

    def put(self, request, pk, room_pk) :
        wishlist = self.get_list(pk=pk)

        if not wishlist.user == request.user :
            raise exceptions.PermissionDenied
        
        room = self.get_room(pk=room_pk)

        if wishlist.rooms.filter(pk=room_pk).exists() :
            wishlist.rooms.remove(room)
        else :
            wishlist.rooms.add(room)

        return Response(status.HTTP_200_OK)
