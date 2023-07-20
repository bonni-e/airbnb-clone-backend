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

class UserRequestSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = (
            "name",
            "username",
            "password",
            "email",
        )


class PrivateUserSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = "__all__"

        # exclude = (
        #     "password",
        # )