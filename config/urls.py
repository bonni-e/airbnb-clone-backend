"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("tweets.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include("users.urls")),
    path('api/v1/rooms/', include("rooms.urls")),
    path('api/v1/tweets/', include("tweets.urls")),
    path('api/v1/experiences/', include("experiences.urls")),
    path('api/v1/categories/', include("categories.urls")),
    path('api/v1/medias/', include("medias.urls")),

]

# 개발 단계에서만 사용할 것을 권장 (보안상의 문제)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)