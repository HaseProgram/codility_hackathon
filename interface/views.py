from django.http import HttpResponse, Http404, HttpResponseRedirect
from  django.template import loader
from django.template import Template
from django.shortcuts import render, render_to_response
from interface.form import LoginForm
# Create your views here.
def signin(request):
	 return render(request, "signin.html",{})
