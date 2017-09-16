from django.http import HttpResponse, Http404, HttpResponseRedirect
from  django.template import loader
from django.template import Template
from django.shortcuts import render, render_to_response
from interface.form import LoginForm
from django.contrib.auth.decorators import login_required
import json 
from interface.openapi import getcardlist
# Create your views here.

def signin(request):
    redirect = request.GET.get('continue', '/')
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
    #redirect = request.GET.get('continue', '/signin')
    cardsList = json.loads(getcardlist())
    return HttpResponseRedirect()
