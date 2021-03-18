from .serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from .mixins.rest import CreateListMixin
from .models import Photo
from django.http import HttpResponse

from .computer_vision.face_detection import face_detection


class PhotoViewSet(CreateListMixin, ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    print("==>")
    print(queryset)
    print("<==")


def p(request):
    p = Photo.objects.get(id=1)
    face_detection(p.photo_b64)
    return HttpResponse('ok')
