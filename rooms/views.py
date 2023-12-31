from datetime import date, timedelta
from typing import Any
from django.utils import timezone
from django.conf import settings
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied, ValidationError
from rest_framework import status
from categories.models import Category
from .models import Room, Amenity
from reviews.models import Review
from medias.models import Photo
from bookings.models import Booking
from .serializers import *
from reviews.serializers import ReviewSerializer
from medias.serializers import *
from bookings.serializers import *
from reviews.pagenations import StandardResultsSetPagination

class RoomBookings(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk) :
        try : 
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist :
            raise NotFound

    # 예약 조회 
    def get(self, request, pk) :
        room = self.get_object(pk)
        now = timezone.localtime().date()
        print("now : ", now)
        
        bookings = Booking.objects.filter(room__pk=pk, kind=Booking.BookingKundChoices.ROOM, check_in__gte=now)
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    # 예약 생성 
    def post(self, request, pk) :
        room = self.get_object(pk)
        serializer = RoomBookingSerializer(data=request.data)
        
        if serializer.is_valid() :
            with transaction.atomic() :
                serializer.save(user=request.user, room=room, kind=Booking.BookingKundChoices.ROOM)

                check_in = serializer.data['check_in']
                check_out = serializer.data['check_out']

                bookings = Booking.objects.filter(room__pk=pk, check_in__lt=check_out, check_out__gt=check_in)

                if len(bookings) > 1 :
                    raise ValidationError("노노노~")
            
                return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomPhotos(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk) :
        try :
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist :
            raise NotFound

    def post(self, request, pk) :
        room = self.get_object(pk)

        if not room.owner == request.user :
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid() :
            with transaction.atomic() :
                photo = serializer.save(room=room)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
    
    # def delete(self, request, pk, photo_pk) :
    #     room = self.get_object(pk)

    #     if not room.owner == request.user :
    #         raise PermissionDenied
        
    #     try :
    #         photo = room.photos.get(pk=photo_pk)
    #         photo.delete()
    #     except Photo.DoesNotExist :
    #         raise NotFound
        
    #     return Response(status.HTTP_204_NO_CONTENT)
        

class RoomReviews(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk) :
        try :
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist :
            raise NotFound

    def get(self, request, pk) :
        # 파라미터 값 가져오기 
        # params :  <QueryDict: {'page': ['1']}>
        params = request.query_params   
        print("params : ", params)

        try :
            page = params.get("page", 1) # 디폴트 값 1 
            print("page : ",  type(page))
            page = int(page)
            print("page : ",  type(page))
        except ValueError :
            page = 1

        room = self.get_object(pk)

        # 페이지네이션 처리 1.
        # ㄴ 슬라이싱 활용 
        # ㄴ OFFSET A LIMIT B 구문을 수행함 

        start = (page - 1) * settings.PAGE_SIZE
        end = start + settings.PAGE_SIZE
        reviews = room.reviews.all()[start:end]

        if len(reviews) == 0 :
            raise ValidationError
        
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    # 리뷰 작성 
    def post(self, request, pk) :
        room = self.get_object(pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid() :
            if not room.owner == request.user :
                serializer.save(user=request.user, room=room)
            else :
                raise PermissionDenied
        return Response(serializer.data)
    
# 페이지네이션 처리 2.
class RoomReviewPagenation(ListAPIView) :
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        try :
            pk = request.query_params.get('room')
            room = Room.objects.get(pk=pk)
            self.queryset = room.reviews.all()
        except Room.DoesNotExist :
            raise NotFound
        
        return super().get(request, *args, **kwargs)
    
class RoomAmenities(APIView) :
    def get_object(self, pk) :
        try :
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist :
            raise NotFound

    def get(self, request, pk) :
        room = self.get_object(pk)

        page = request.query_params.get('page', 1)
        try :
            page = int(page)
        except ValueError :
            page = 1
        
        start = (page - 1) * settings.PAGE_SIZE 
        end = start + settings.PAGE_SIZE
        amenities = room.amenities.all()[start:end]

        if len(amenities) == 0 :
            raise ValidationError

        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data)


class Rooms(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request) :
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True, context={
            "request" : request
        })
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

            if not amenities_pk and isinstance(amenities_pk, list) :
                for pk in amenities_pk :
                    try :
                        amenity = Amenity.objects.get(pk=pk)
                        amenities.append(amenity)
                        # room.amenities.add(amenity)
                    except Amenity.DoesNotExist :
                        # raise ParseError('Amenity is not found.')
                        pass
        
            try :
                # django db에 즉시 반영하지 않고, 변경 사항을 리스트업 -> 에러가 없는 경우에 푸시
                with transaction.atomic() :
                    room = serializer.save(owner=request.user, category=category, amenities=amenities)
                    serializer = RoomSerializer(room, context={
                        "request" : request
                    })
                    return Response(serializer.data)
            except Exception :
                raise ParseError

        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetail(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk) :
        try :
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist :
            raise NotFound

    def get(self, request, pk) :
        room = self.get_object(pk)
        serializer = RoomSerializer(room, context={
            "request" : request
        })
        return Response(serializer.data)

    def put(self, request, pk) :
        room = self.get_object(pk)

        if not room.owner == request.user :
            raise PermissionDenied("나쁜 사람~")
        
        serializer = RoomSerializer(instance=room, data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) :
        room = self.get_object(pk)

        if not room.owner == request.user :
            raise PermissionDenied("나쁜 사람~")
        
        room.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class Amenities(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticated]

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