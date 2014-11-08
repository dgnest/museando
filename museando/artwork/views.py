from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtworkSerializer
from .models import Artwork


class ArtworkViewSet(viewsets.ModelViewSet):

    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )
    filter_fields = (
        'museum',
        'name',
        'uid',
        'author',
        'style',
    )
