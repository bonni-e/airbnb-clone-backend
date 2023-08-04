from django.db import models
from django.contrib.auth.models import AbstractUser;

# Create your models here.
# class User(models.Model) :
#     pass

class User(AbstractUser) :
    # 필드값 옵션 넣기 
    class GenderChoices(models.TextChoices) :
        MAIL = ("male", "Male") # (필드값, 관리자페이지에서보이는라벨명)
        FEMAIL = ("female", "Female")

    class LanguageChoices(models.TextChoices) :
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices) :
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")


    # 디폴트 필드값을 유령으로 만들기 (editable=False)
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 나만의 이름 필드 만들기 
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    # is_host = models.BooleanField(null=True)    # nullable field
    # default 속성으로 기존 값을에 대한 처리를 정해줌

    avatar = models.ImageField(blank=True) # profile_photo

    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default='kr')
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices, default='won')