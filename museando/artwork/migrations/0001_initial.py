# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import artwork.models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=450)),
                ('uid', models.CharField(max_length=32, blank=True)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50, blank=True)),
                ('style', models.CharField(max_length=50, blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=artwork.models.upload_photo_to, verbose_name='image')),
                ('museum', models.ForeignKey(verbose_name='museum', to='museum.Museum')),
            ],
            options={
                'db_table': 'artwork',
                'verbose_name': 'artwork',
                'verbose_name_plural': 'artworks',
            },
            bases=(models.Model,),
        ),
    ]
