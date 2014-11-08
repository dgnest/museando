from django.db import models
from django.conf import settings
from django.utils import timezone
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def upload_photo_to(self, filename):
    url = (
        "artwork/%(name)s/%(filename)s"
    ) % {
        "name": self.name,
        "filename": filename,
    }
    return url


class Artwork(models.Model):
    museum = models.ForeignKey(
        'museum.Museum',
        verbose_name=_('museum'),
    )
    name = models.CharField(
        max_length=450,
    )
    uid = models.CharField(
        max_length=32,
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    author = models.CharField(
        max_length=50,
        blank=True,
    )
    style = models.CharField(
        max_length=50,
        blank=True,
    )
    image = ProcessedImageField(
        upload_to=upload_photo_to,
        processors=[
            ResizeToFill(width=628, height=420),
        ],
        format='PNG',
        verbose_name=_('image'),
    )

    def _get_image(self):
        return str(self.image.url)

    image_url = property(_get_image)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'artwork'
        verbose_name = _('artwork')
        verbose_name_plural = _('artworks')
