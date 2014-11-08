from rest_framework import serializers
from .models import Museum


class MuseumSerializer(serializers.ModelSerializer):
    image_profile = serializers.ImageField(
        allow_empty_file=False,
        required=True,
    )
    image_profile_url = serializers.Field()
    image_list = serializers.ImageField(
        allow_empty_file=False,
        required=True,
    )
    image_list_url = serializers.Field()

    class Meta:
        model = Museum
        fields = (
            'id',
            'user',
            'uid',
            'name',
            'description',
            'district',
            'address',
            'schedule',
            'price',
            'image_profile',
            'image_profile_url',
            'image_list',
            'image_list_url',
            'telephone',
            'email',
            'website',
            'is_active',
        )
