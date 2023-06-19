from django.contrib import admin
from .models import House

# Register your models here.

# HouseAdmin 클래스가 House 모델을 통제할 것이라고 decorator함 (Admin 패널 생성)
@admin.register(House)
class HouseAdmin(admin.ModelAdmin) :
    # 모델의 필드값들로 구성
    # 리스트[] 또는 튜플()로 작성 
    # ㄴ one item tuple 인 경우, 맨 뒤에 ,콤마 붙여서 자동으로 문자열 처리되지 않도록 하기
    
    # 목록 생성 
    list_display = (
        "name", 
        "price_per_night",
        "address",
        "pet_allowed"
    )

    # list_display = (
    #     "name", 
    #     "price_per_night", 
    #     ("address", "pet_allowed") # 어드민 패널 폼 양식에서 같은 행에 여러 열로 배치됨
    # )

    # 필터 생성 
    list_filter = (
        "price_per_night",
        "pet_allowed"
    )

    # 검색 필드 등록 
    search_fields = (
        # "address"
        "address__startswith",   # 검색어로 시작하는 조건도 설정 가능 
    )

    # (어드민 패널에서의) 수정 제외 필드 
    # exclude = (
    #     "price_per_night",
    # )