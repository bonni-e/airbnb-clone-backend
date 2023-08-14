from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import * 

class PhotoDetail(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk) :
        try :
            photo = Photo.objects.get(pk=pk)
            return photo
        except Photo.DoesNotExist :
            raise exceptions.NotFound

    def delete(self, request, pk) :
        photo = self.get_object(pk)

        if((photo.room and photo.owner != request.user) or (photo.experience and photo.experience.host != request.user)) :
            raise exceptions.PermissionDenied
        
        photo.delete()
        return Response(status.HTTP_204_NO_CONTENT)
