# REST Framework 사용 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .models import Category

'''
리팩토링 2 후

class CategoryViewSet(ModelViewSet) :
    serializer_class = CategorySerializer
    queryset = Category.objects.all() 
'''

'''
리팩토링 1 후  
'''

class Categories(APIView) :
    def get(self, request) :
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print('serializer : ', serializer)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid() :
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else :
            return Response(serializer.errors)

class CategoryDetail(APIView) :
    def get_object(self, pk) :
        try :
            category = Category.objects.get(pk=pk)  
            return category
        except Category.DoesNotExist :
            raise NotFound 

    def get(self, request, pk) :
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def post(self, request, pk) :
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid() : 
            update_category = serializer.save() # -> update() 메소드 호출 
            return Response(CategorySerializer(update_category).data)
        else : 
            return Response(serializer.errors)
        
    def delete(self, request, pk) :
        category = self.get_object(pk)
        category.delete()
        return Response(HTTP_204_NO_CONTENT)


'''
리팩토링 전 

# 장고 데코레이터 
@api_view(["GET", "POST"])
def categories(request) :
    if request.method == "GET" :
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST" :
        # print(request.data)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid() :
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else :
            return Response(serializer.errors)
    
@api_view(["GET", "PUT", "DELETE"])
def category(request, pk) :
    try : 
        category = Category.objects.get(pk=pk)  
        if request.method == "GET" :
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        elif request.method == "PUT" :
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid() : 
                update_category = serializer.save() # -> update() 메소드 호출 
                return Response(CategorySerializer(update_category).data)
            else : 
                return Response(serializer.errors)
        elif request.method == "DELETE" :
            category.delete()
            return Response(HTTP_204_NO_CONTENT)
    except Category.DoesNotExist :
        raise NotFound

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
'''