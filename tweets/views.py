from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializer

def get_all_tweets(request) :
    tweets = Tweet.objects.all()
    return render(request, "tweets.html", {
        "tweets" : tweets,
        "title" : "All Tweets"
    })

class Tweets(APIView) :
    def get(self, request) :
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

class TweetDetail(APIView) :
    def get_obgject(self, pk) :
        try :
            tweet = Tweet.objects.get(pk=pk)
            return tweet
        except Tweet.DoesNotExist :
            raise NotFound

    def get(self, request, pk) : 
        tweet = self.get_obgject(pk) 
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk) : 
        tweet = self.get_obgject(pk) 
        serializer = TweetSerializer(instance=tweet, data=request.data, partial=True)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

    def delete(self, request, pk) : 
        tweet = self.get_obgject(pk) 
        tweet.delete()
        return Response(status.HTTP_204_NO_CONTENT)
