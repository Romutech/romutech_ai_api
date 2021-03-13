from .serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from .mixins.rest import CreateListMixin
from .models import Photo


class PhotoViewSet(CreateListMixin, ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
