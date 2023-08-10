from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import status
from categories.models import Category
from .models import Room, Amenity
from .serializers import *


class Rooms(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request) :
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid() :
            print("request.data : ", request.data)
            category_pk = request.data.get("category")
            if not category_pk :
                raise ParseError('Category is required.')
            
            try :
                category = Category.objects.get(pk=category_pk)
            except Category.DoesNotExist :
                raise ParseError('Category is not found.')
            
            amenities_pk = request.data.get("amenities")
            amenities = []
            for pk in amenities_pk :
                try :
                    amenity = Amenity.objects.get(pk=pk)
                    amenities.append(amenity)
                except Amenity.DoesNotExist :
                    raise ParseError('Amenity is not found.')
            
            room = serializer.save(owner=request.user, category=category, amenities=amenities)

            # room.amenities.add(amenity)

            return Response(RoomSerializer(room).data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetail(APIView) :
    def get_object(self, pk) :
        try :
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist :
            raise NotFound

    def get(self, request, pk) :
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk) :
        room = self.get_object(pk)
        serializer = RoomSerializer(instance=room, data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk) :
        room = self.get_object(pk)
        room.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class Amenities(APIView) :
    def get(self, request) :
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class AmenityDetail(APIView) :
    def get_object(self, pk) :
        try :
            amenity = Amenity.objects.get(pk=pk)
            return amenity
        except Amenity.DoesNotExist :
            raise NotFound
   
    def get(self, request, pk) :
        amenity = self.get_object(pk)
        return Response(AmenitySerializer(amenity).data)

    def put(self, request, pk) :
        amenity = self.get_object(pk) 
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)

        if serializer.is_valid() :
            serializer.save() 
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) :
        amenity = self.get_object(pk)  
        amenity.delete()
        return Response(status.HTTP_204_NO_CONTENT)

'''
def see_all_rooms(request) :
    rooms = Room.objects.all() 
    # return render(request, "rooms.html")
    # 데이터 담아 보내기 
    return render(request, "rooms.html", {
        "rooms" : rooms,
        "title" : "Hello! this title comes from django!"
        }) 

def see_one_rooms(request, room_pk) :
    try :
        room = Room.objects.get(pk=room_pk)
        return render(request, "room_detail.html", {"room" : room})
    except Room.DoesNotExist : 
        # return render(request, "404.html")
        return render(request, "room_detail.html", {"not_found" : True})
'''