from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin) :
#     pass

@admin.register(User)
class CustomUserAdmin(UserAdmin) :
    fieldsets = (
        ("Profile", 
            {
                "fields" : ("username", "password", "name", "email", "is_host")
            },
        ),
        ("Permissions",
         {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes" : ("collapse", ) # 토글로 접기 
            },
        ),
        ("Important dates",
        {  "fields" :
             ("last_login", "date_joined"),
            "classes" : ("collapse", ) # 토글로 접기 
         }
        )
    )

    list_display = ("username", "email", "name", "is_host")