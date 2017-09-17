from django.http import HttpResponse, Http404, HttpResponseRedirect
from  django.template import loader
from django.template import Template
from django.shortcuts import render, render_to_response
from interface.form import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import json 
#from interface.openapi import getcardlist

def signin(request):
    redirect = request.GET.get('continue', '/')
    print(redirect)
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            return HttpResponseRedirect(redirect)
    else:
        form = LoginForm()

    return render(request, 'signin.html', {
            'form': form,
})


@login_required(redirect_field_name='continue')
def index(request):
    #redirect = request.GET.get('continue', '/')
    #cardsList = json.loads(getcardlist())
    print('hello')
    return HttpResponse()


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'index.html', {
            'form': form,
            })

@login_required(redirect_field_name='continue')
def logout(request):
    redirect = request.GET.get('continue', '/')
    auth.logout(request)
    return HttpResponseRedirect(redirect)

def Main