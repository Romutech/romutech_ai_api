from .serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from .mixins.rest import CreateListMixin
from .models import Photo
from django.http import HttpResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .computer_vision.face_detection import face_detection


@api_view(['POST'])
def photo_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'POST':
        photo = Photo(photo_b64=request.POST['photo_b64'])
        photo.save()
        face(photo)


        return HttpResponse('ok')
        return Response(request.POST['photo_b64'], status=status.HTTP_201_CREATED)


class PhotoViewSet(CreateListMixin, ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


def face(photo):
    print(photo.photo_b64)
    face_detection(str(photo.photo_b64))

    #p = Photo.objects.get(id=1)
    #face_detection(p.photo_b64)
    #return HttpResponse('ok')
