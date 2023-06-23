from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin) :
    list_display = (
        "__str__",  # 모델의 str 메서드를 보여주기 위함 
        "payload",

    )

    list_filter = (
        "rating",
    )