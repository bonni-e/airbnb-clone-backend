from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

def get_all_tweets(request) :
    tweets = Tweet.objects.all()
    return render(request, "tweets.html", {
        "tweets" : tweets,
        "title" : "All Tweets"
    })
