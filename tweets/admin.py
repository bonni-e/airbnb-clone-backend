from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Tweet, Like

class WordFilter(admin.SimpleListFilter) :
    title = "Contains Elon Musk"
    parameter_name = "elon"

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ("true", "Contains Elon Musk"),
            ("false", "Not contains Elon Musk"),
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        word = self.value()

        if not word :
            return None
        elif word == 'true' :
            return queryset.filter(payload__contains='elon musk')
        else :
            return queryset.exclude(payload__contains='elon musk')
        

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
        WordFilter,
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