from django.conf.urls import patterns, url
from .views import artwork_list, ArtworkDetailView, ArtworkDeleteView
from .views import artwork_create, artwork_update


urlpatterns = patterns(
    '',
    url(r'^$', artwork_list, name='artwork-list'),
    url(r'^create/$', artwork_create, name='artwork-create'),
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
    url(
        r'^update/(?P<pk>[\w]+)/$',
        artwork_update,
        name='artwork-update',
    ),
)
