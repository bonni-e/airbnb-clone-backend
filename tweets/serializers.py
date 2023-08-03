from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Tweet
        fields = "__all__"

# class TweetSerializer(serializers.Serializer) :
#     pk = serializers.IntegerField()
#     payload = serializers.CharField()
#     user = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     modified_at = serializers.DateTimeField()
