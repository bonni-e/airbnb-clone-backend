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
        "user",
        "created_at",
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

    # search_fields = [
    #     "user_key"
    # ]

    # def user_key(self, like) :
    #     return like.user__user_pk