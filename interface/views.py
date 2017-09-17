from django.http import HttpResponse, Http404, HttpResponseRedirect
from  django.template import loader
from django.template import Template
from django.shortcuts import render, render_to_response
from interface.form import LoginForm, SignupForm
from interface.models import Profile, Card
from interface.openapi import OpenAPI
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
        	request.session['fakecard'] = Profile.objects.filter(user_id=request.user.id)[0].get_fakecard()
            auth.login(request, form.cleaned_data['user'])
            return HttpResponseRedirect(redirect)
    else:
        form = LoginForm()

    return render(request, 'signin.html', {
            'form': form,
})


#@login_required(redirect_field_name='continue')
def index(request):
    oapi = OpenAPI()
    cards = oapi.getcardlist()
    cardslist = []
    for card in cards['Card']:
        balance = oapi.getbalance(card['CardId'])
        tCard = Card()
        tCard.balance = balance['Value']
        cardslist.append(tCard)
        fakeCard = request.session['fakecard']
        transaktions = oapi.gettransactions(card['CardId'])
        print(transaktions)

    return HttpResponse()


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            request.session['fakecard'] = Profile.objects.filter(user_id=request.user.id)[0].get_fakecard()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
            'form': form,
            })

@login_required(redirect_field_name='continue')
def logout(request):
    redirect = request.GET.get('continue', '/')
    auth.logout(request)
    return HttpResponseRedirect(redirect)
