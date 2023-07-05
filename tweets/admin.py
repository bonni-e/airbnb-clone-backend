from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin) :
    list_display = (
        "user",
        "payload",
        "likes_count",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "payload",
        "^user__username",
    )

    # def likes(self, tweet) :
    #     return tweet.like_set.all().count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin) :
    list_display = (
        "user",
        "tweet",
        "created_at",
        "modified_at",
    )

    list_filter = [
        "created_at",
    ]

    search_fields = [
        "^user__username",
    ]

    # def user_key(self, like) :
    #     return like.user__user_pk