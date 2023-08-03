from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import status
from .models import User
from .serializer import *
from tweets.serializers import *

class Me(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request) :
        user = request.user
        print('\n\n>>>')
        print(user)
        print(dir(user))
        print('<<<\n\n')
        return Response({})

class Users(APIView) :
    def get(self, request) :
        users = User.objects.all()
        serializer = PrivateUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = UserRequestSerializer(data= request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
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
        except User.DoesNotExist :
            return Response(exceptions.NotFound)

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
    
