from django.conf.urls import patterns, url
from .views import artwork_list, ArtworkDetailView, ArtworkDeleteView


urlpatterns = patterns(
    '',
    url(r'^$', artwork_list, name='artwork-list'),
    url(
        r'^(?P<pk>[\w]+)/$',
        ArtworkDetailView.as_view(),
        name='artwork-detail',
    ),
    url(
        r'^delete/(?P<pk>[\w]+)/$',
        ArtworkDeleteView.as_view(),
        name='artwork-delete',
    ),
    # url(r'^update/$', museum_update, name='museum-update'),
)
