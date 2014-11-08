from django import forms
from django.contrib.auth.models import User
from museum.models import Museum


class RegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
    )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(
        max_length=100,
    )
    password2 = forms.CharField(
        max_length=100,
    )
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')

        if username and first_name and last_name and email and \
                password1 and password2 and name and address:
            try:
                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.set_password(password2)
                user.save()

                museum = Museum.objects.create(
                    user=user,
                    name=self.cleaned_data["name"],
                    address=self.cleaned_data["address"],
                )

                return self.cleaned_data
            except Exception, e:
                pass
