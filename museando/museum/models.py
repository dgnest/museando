from django.db import models
from django.conf import settings
from django.utils import timezone
from imagekit.processors import ResizeToFit, ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def upload_photo_to(self, filename):
    url = (
        "museums/%(id)s/%(filename)s"
    ) % {
        "id": self.id,
        "filename": filename,
    }
    return url


class Museum(models.Model):
    name = models.CharField(
        max_length=450
    )
    description = models.TextField()
    district = models.CharField(
        max_length=50
    )
    schedule = models.CharField(
        max_length=100
    )
    image_profile = ProcessedImageField(
        upload_to=upload_photo_to,
        processors=[
            ResizeToFill(width=500, height=200),
        ],
        format='PNG',
        verbose_name=_('image profile'),
    )
    image_list = ProcessedImageField(
        upload_to=upload_photo_to,
        processors=[
            ResizeToFill(width=100, height=60),
        ],
        format='PNG',
        verbose_name=_('image list'),
    )

    def _get_image_profile(self):
        return str(self.image_profile.url)

    image_profile_url = property(_get_image_profile)

    def _get_image_list(self):
        return str(self.image_list.url)

    image_list_url = property(_get_image_list)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'museum'
        verbose_name = _('museum')
        verbose_name_plural = _('museums')
