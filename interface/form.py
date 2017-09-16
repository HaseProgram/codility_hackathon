from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from interface.models import Profile
from django.core.files import File
from django import forms
import urllib

class LoginForm(forms.Form):
    login = forms.CharField(
            widget=forms.TextInput(
                attrs={ 'class': 'form-control', 'placeholder': 'login', 'autocomplete' : 'off'}
                ),
            max_length=30,
            label=u'Login'
            )

    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={ 'class': 'form-control', 'type': 'password', 'placeholder': 'password', 'autocomplete' : 'off'}),
            label=u'Password'
            )

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get('login', ''), password=data.get('password', ''))
        if user is not None:
            if user.is_active:
                data['user'] = user
            else:
                raise forms.ValidationError(u'This user don\'t active')
        else:
            raise forms.ValidationError(u'Uncorrect login or password')
