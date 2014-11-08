from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework import routers
from django.contrib import admin

from museum.views import MuseumViewSet
from artwork.views import ArtworkViewSet


router = routers.DefaultRouter()
router.register(r'museums', MuseumViewSet)
router.register(r'artworks', ArtworkViewSet)

urlpatterns = patterns(
    '',
    # Grappelli urls.
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Browsable API.
    url(r'^api/', include(router.urls)),
    # Token Authentication.
    url(
        r'^api-token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token',
    ),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )
