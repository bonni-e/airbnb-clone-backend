from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )

class UserSerializer(ModelSerializer) :
    class Meta :
        model = User
        # fields = "__all__"

        exclude = (
            "password",
        )