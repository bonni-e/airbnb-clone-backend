from django.contrib import admin
from .models import Photo, Video

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin) :
    pass

@admin.register(Photo)
class VideoAdmin(admin.ModelAdmin) :
    pass