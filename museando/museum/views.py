from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .serializers import MuseumSerializer
from .models import Museum


class MuseumViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    filter_fields = (
        'name',
        'uid',
        'district',
        'is_active',
    )


@csrf_protect
@login_required(login_url=settings.LOGIN_URL, redirect_field_name='next')
def museum_detail(request):
    try:
        museum = Museum.objects.get(user=request.user.id)
    except Exception, e:
        museum = None
    ctx = {
        'museum': museum,
    }
    return render_to_response(
        'museum/detail.html',
        ctx,
        context_instance=RequestContext(request),
    )


def update_museum(request):
    user = request.user
    name = request.POST['name']
    description = request.POST['description']
    district = request.POST['district']
    address = request.POST['address']
    schedule = request.POST['schedule']
    price = request.POST['price']
    image_profile = request.FILES.get('image_profile')
    image_list = request.FILES.get('image_list')
    telephone = request.POST['telephone']
    email = request.POST['email']
    website = request.POST['website']

    museum = get_object_or_404(Museum, user=user.id)

    museum.name = name
    museum.description = description
    museum.district = district
    museum.schedule = schedule
    museum.price = price
    museum.image_profile = image_profile
    museum.image_list = image_list
    museum.telephone = telephone
    museum.email = email
    museum.website = website
    museum.save()
    return museum


@csrf_protect
@login_required(login_url=settings.LOGIN_URL, redirect_field_name='next')
def museum_update(request):
    museum = Museum.objects.get(user=request.user.id)
    ctx = {
        'museum': museum,
    }

    if request.method == "POST":
        medicine = update_museum(request)
        if medicine:
            return HttpResponseRedirect(reverse('museum_app:museum-detail'))

    return render_to_response(
        'museum/update.html',
        ctx,
        context_instance=RequestContext(request),
    )
