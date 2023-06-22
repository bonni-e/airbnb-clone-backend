from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin) :
    list_display = (
        "user",
        "payload",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "user",
        "created_at",
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin) :
    list_display = (
        "user",
        "tweet",
        "created_at",
        "modified_at",
    )

    list_filter = (
         "created_at",
    )