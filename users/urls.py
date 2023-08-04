from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
    path("<int:pk>/tweets", UserTweets.as_view()),
    path("login", Login.as_view()),
    path("token-login", ObtainAuthToken.as_view()),
    path("logout", Logout.as_view()),
    path("password", Password.as_view()),

]