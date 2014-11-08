from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtworkSerializer
from .models import Artwork
from museum.models import Museum

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class ArtworkViewSet(viewsets.ModelViewSet):

    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )
    filter_fields = (
        'museum',
        'name',
        'uid',
        'author',
        'style',
    )


@csrf_protect
@login_required(login_url=settings.LOGIN_URL, redirect_field_name='next')
def artwork_list(request):
    artworks = None
    search = request.GET.get("search", False)

    try:
        museum = Museum.objects.get(user=request.user)
        if museum.is_active:
            if search:
                try:
                    artworks = Artwork.objects.filter(name__icontains=search) | \
                        Artwork.objects.filter(uid__icontains=search)
                except Exception, e:
                    artworks = None
            else:
                artworks = Artwork.objects.filter(museum=museum)
        else:
            artworks = None
    except Exception, e:
        museum = None
        artworks = None

    ctx = {
        'artworks': artworks,
        'museum': museum,
    }

    return render_to_response(
        'artwork/list.html',
        ctx,
        context_instance=RequestContext(request),
    )


class ArtworkDetailView(LoginRequiredMixin, DetailView):
    model = Artwork
    template_name = 'artwork/detail.html'


class ArtworkDeleteView(LoginRequiredMixin, DeleteView):
    model = Artwork
    success_url = reverse_lazy('artwork_app:artwork-list')
    template_name = 'artwork/delete.html'
