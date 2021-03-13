from .serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Photo


class PhotoViewSet(ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
