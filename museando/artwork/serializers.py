from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        allow_empty_file=False,
        required=True,
    )
    image_url = serializers.Field()

    class Meta:
        model = Artwork
        fields = (
            'id',
            'museum',
            'name',
            'uid',
            'description',
            'author',
            'style',
            'image',
            'image_url',
        )
