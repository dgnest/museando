from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .forms import RegistrationForm


def home(request, ctx=None):

    if not ctx:
        ctx = {}
        ctx['message'] = _("Welcome")

    return render_to_response(
        'home/home.html',
        ctx,
        context_instance=RequestContext(request),
    )


def login(request):
    if request.user.is_authenticated():
        return home(request)

    message = ""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return home(request)
        else:
            message = _("Incorrect username or password")

    ctx = {
        'message': message,
    }
    return render_to_response(
        'home/login.html',
        ctx,
        context_instance=RequestContext(request),
    )


def record_user(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    is_superuser = request.POST.get('is_superuser', False)

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_superuser=is_superuser,
    )
    user.set_password(password)
    user.save()

    return user


def signup(request):
    if request.user.is_authenticated():
        return home(request)

    message = ""
    errors = ""
    ctx = {}
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                ctx['message'] = _("Wait to be activated")
                return home(request, ctx)
        else:
            errors = form.errors
            message = _("Incorrect username or password")

    ctx = {
        'errors': errors,
        'message': message,
    }
    return render_to_response(
        'home/signup.html',
        ctx,
        context_instance=RequestContext(request),
    )


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home_app:login'))
