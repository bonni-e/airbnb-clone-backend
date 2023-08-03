from django.urls import path
from .views import *

urlpatterns = [
    path("", Tweets.as_view()),
    path("<int:pk>/", TweetDetail.as_view()),
]