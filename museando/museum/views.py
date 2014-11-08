from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MuseumSerializer
from .models import Museum


class MuseumViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    filter_fields = (
        'name',
        'district',
    )
