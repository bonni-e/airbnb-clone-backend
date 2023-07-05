from django.contrib import admin
from .models import Review

# 필터 커스터마이징하기 
class WordFilter(admin.SimpleListFilter) :
    title = "Filter by words!"
    parameter_name = "potato"

    def lookups(self, request, model_admin) :
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]
    
    def queryset(self, request, reviews) :
        # print(dir(request))
        # print(request.GET)    # <QueryDict: {'potato': ['good']}>
        word = self.value()     # good

        # if(word == None) :
        if(not word) :
            return reviews.all()
        
        return reviews.filter(payload__contains=word)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin) :
    list_display = (
        "__str__",  # 모델의 str 메서드를 보여주기 위함 
        "payload",

    )

    list_filter = (
        WordFilter,
        "rating",
        # "user",
        # "user__username",     # FK 기반으로 필터링 할 수 있음 
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )