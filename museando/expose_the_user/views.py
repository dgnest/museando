from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    filter_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )
