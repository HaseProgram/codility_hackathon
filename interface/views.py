from django.http import HttpResponse, Http404, HttpResponseRedirect
from  django.template import loader
from django.template import Template
from django.shortcuts import render, render_to_response
from interface.form import LoginForm, SignupForm
from interface.models import Profile, Card, Transaction
from interface.openapi import OpenAPI, BadResponseError
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from random import randint
import json 

def signin(request):
    redirect = request.GET.get('continue', '/')
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            profile = Profile.objects.get_or_create(request.user.id)
            request.session['fakecard'] = profile.get_fakecard()
            return HttpResponseRedirect(redirect)
    else:
        form = LoginForm()

    return render(request, 'signin.html', {
            'form': form,
})

@login_required(redirect_field_name='continue')
def index(request):
    oapi = OpenAPI()
    userlist = Profile.objects.get_profiles_by_id(request.user.id)
    try:
        cards = oapi.get_cardlist()
        cardslist = []
        for card in cards['Card']:
            balance = oapi.get_balance(card['CardId'])
            tCard = Card()
            tCard.balance = balance['Value']
            cardslist.append(tCard)
            fakeCard = request.session['fakecard']
            transactions = oapi.get_transactions(card['CardId'])
            for transaction in transactions:
                Transaction.objects.generate_transaction(transaction, request.user.id)
            transactionlist = Transaction.objects.get_by_userid(request.user.id)
            cardlist = None
        return render(request, 'index.html', { 'transactionlist' : transactionlist, 'userlist' : userlist, 'cardlist' : cardlist })
    except BadResponseError:
        message = 'Error with api'
        return render(request, 'error.html', {
            'message': message 
})

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

@login_required(redirect_field_name='continue')
def publictransaction(request):
    redirect = request.GET.get('continue', '/')
    body = request.body.decode("utf-8")
    request.POST = json.loads(body)
    transaction = Transaction.objects.get(transactionId=request.POST.get('tid', False))
    is_public = request.POST.get('checked', False)
   	print(is_public)
    transaction.public = is_public
    transaction.save()

    return HttpResponse(
        json.dumps({"tid": request.POST['tid'], 'public': is_public}),
        content_type="application/json"
)


@login_required(redirect_field_name='continue')
def contact(request, id):
    redirect = request.GET.get('continue', '/')
    requested_contact = Profile.objects.filter(user_id=id)
    if requested_contact.count > 0:
        fake_card = requested_contact[0].get_fakecard()
    else:
        Http404()
    return render(request, 'contact.html', { 'fakecard' : fakecard, 'form': form})
    