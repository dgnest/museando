from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
    )
    first_name = serializers.Field()
    last_name = serializers.Field()
    is_active = serializers.Field()
    is_staff = serializers.Field()
    is_superuser = serializers.Field()
    date_joined = serializers.Field()
    last_login = serializers.Field()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        """
        Instantiate a new User instance.
        """
        user = User(email=attrs['email'], username=attrs['username'])
        user.set_password(attrs['password'])
        return user
