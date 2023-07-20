from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import *
from .serializers import * 

class Perks(APIView) :
    def get(self, request) :
        perks = Perk.objects.all()
        serializer = PerkSerializer(perks, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

class PerkDetail(APIView) :
    def get_object(self, pk) :
        try :
            perk = Perk.objects.get(pk=pk)
            return perk
        except Perk.DoesNotExist :
            return NotFound

    def get(self, request, pk) :
        perk = self.get_object(pk)
        return Response(PerkSerializer(perk).data)

    def put(self, request, pk) :
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk, data=request.data, partial=True)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

    def delete(self, request, pk) :
        perk = self.get_object(pk)
        perk.delete()
        return Response(status.HTTP_204_NO_CONTENT)