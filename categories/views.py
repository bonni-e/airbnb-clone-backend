# REST Framework 사용 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import Category

@api_view()
def categories(request) :
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({
        'ok' : True,
        'categories' : serializer.data
    })



# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import Category
# from django.core import serializers # ModelSerializer

# # Create your views here.
# def categories(request) :
#     categories = Category.objects.all()
#     # return HttpResponse("hello")  
#     # HttpResponse 를 사용하지 않고 -> JSON 데이터를 응답본문으로 주는 REST API를 만들어보자 
#     return JsonResponse({
#         'ok' : True,
#         # 'categories' : categories 
#         # JSON으로 변환 불가 -> 번역기 Serializer가 필요함 
#         'categories' : serializers.serialize("json", categories)
#     })