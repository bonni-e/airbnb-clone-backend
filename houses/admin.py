from django.contrib import admin
from .models import House

# Register your models here.

# HouseAdmin 클래스가 House 모델을 통제할 것이라고 decorator함 
@admin.register(House)
class HouseAdmin(admin.ModelAdmin) :
    pass