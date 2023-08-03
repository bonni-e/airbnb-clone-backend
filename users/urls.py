from django.urls import path
from .views import *

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
    path("user/<int:pk>", UserDetail.as_view()),
    path("<int:pk>/tweets", UserTweets.as_view())
]