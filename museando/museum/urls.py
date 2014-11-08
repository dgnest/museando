from django.conf.urls import patterns, url
from .views import museum_detail, museum_update


urlpatterns = patterns(
    '',
    url(r'^$', museum_detail, name='museum-detail'),
    url(r'^update/$', museum_update, name='museum-update'),
)
