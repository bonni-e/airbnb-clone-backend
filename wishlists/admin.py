from django.contrib import admin
from .models import Wishlist

# Register your models here.
@admin.register(Wishlist)
class WishListAdmin(admin.ModelAdmin) :
    list_display = (
        "name",
        "user",
        "created_at",
        "modified_at",
    )