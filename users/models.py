from django.db import models
from django.contrib.auth.models import AbstractUser;

# Create your models here.
# class User(models.Model) :
#     pass

class User(AbstractUser) :
    # 디폴트 필드값을 유령으로 만들기 (editable=False)
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 나만의 이름 필드 만들기 
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    # is_host = models.BooleanField(null=True)    # nullable field
    # default 속성으로 기존 값을에 대한 처리를 정해줌 
