# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import museum.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=450)),
                ('description', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('schedule', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image_profile', imagekit.models.fields.ProcessedImageField(upload_to=museum.models.upload_photo_to, verbose_name='image profile')),
                ('image_list', imagekit.models.fields.ProcessedImageField(upload_to=museum.models.upload_photo_to, verbose_name='image list')),
                ('telephone', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('website', models.URLField(max_length=400, blank=True)),
            ],
            options={
                'db_table': 'museum',
                'verbose_name': 'museum',
                'verbose_name_plural': 'museums',
            },
            bases=(models.Model,),
        ),
    ]
