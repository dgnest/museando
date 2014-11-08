from django.conf.urls import patterns, url
from .views import login, logout, signup


urlpatterns = patterns(
    '',
    url(r'^$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
)
