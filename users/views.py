from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import exceptions
from rest_framework import status
from .models import User
from .serializer import *
from tweets.serializers import *

class Login(APIView) :
    def post(self, request) :
        username = request.data.get("username")
        password = request.data.get("password")

        # 장고의 기본 쿠키-세션 인증 
        user = authenticate(request, username=username, password=password)

        if user :
            login(request, user)
            return Response(status.HTTP_200_OK)
        else :
            return Response(status.HTTP_401_UNAUTHORIZED)

class Logout(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self, request) :
        logout(request)
        return Response(status.HTTP_200_OK)

class Password(APIView) :
    permission_classes = [IsAuthenticated]

    def put(self, request) :
        password = request.data.get("password")
        new_password = request.data.get("new_password")

        if not password or not new_password :
            raise exceptions.ParseError

        if not request.user.check_password(password) :
            raise exceptions.ParseError
        
        request.user.set_password(new_password)
        request.user.save()

        return Response(status.HTTP_200_OK)

class Me(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request) :
        user = request.user
        return Response(UserSerializer(user).data)

class Users(APIView) :
    def get(self, request) :
        users = User.objects.all()
        serializer = TinyUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid() :
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(TinyUserSerializer(user).data)
        else :
            return Response(serializer.errors)

class UserDetail(APIView) :
    def get(self, request, pk) :
        user = self.get_object(pk)
        serializer = TinyUserSerializer(user)
        return Response(serializer.data)

    def get_object(self, pk) :
        try :
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist :
            raise exceptions.NotFound

# class UserTweets(ModelViewSet) :
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()

# class UserTweets(ViewSet) :
#     def retrieve(self, request, pk=None) :
#         try :
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist :
#             raise exceptions.NotFound
        
#         queryset = Tweet.objects.filter(user=user)
#         serializer = TweetSerializer(instance=queryset, many=True)
#         return Response(serializer.data)

class UserTweets(APIView) :
    def get(self, request, pk=None) :
        try :
            user = User.objects.get(pk=pk)
        except User.DoesNotExist :
            raise exceptions.NotFound
        
        queryset = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(instance=queryset, many=True)
        return Response(serializer.data)
    
