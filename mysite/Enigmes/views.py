#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django import forms

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render
from .forms import RegisterForm
from .forms import LoginForm
from django.template import RequestContext
from .models import Enigmes

def index(request):
    return render(request, 'Enigmes/accueil.html',locals())


def list_enigmes(request, titreQ):
    try:
        rock = Enigmes.objects.get(numero=titreQ)
    except Enigmes.DoesNotExist:
        raise Http404("Globiboulga")
    return render(request, 'Enigmes/maenigme.html', {'question': rock})


def connexion(request):
    if request.method == 'POST':
        formLogin = LoginForm(request.POST)
        if formLogin.is_valid():
            user = authenticate(username=request.POST('username'), password=request.POST('password'))
            if user is not None:
                login(request, user)
                return redirect(deconnexion)
            else:
                return redirect(index)
    else:
        formLogin = LoginForm()
    formRegister = RegisterForm()
    return render(request, 'Enigmes/connexion.html', {'formRegister': formRegister, 'formLogin': formLogin})


def deconnexion(request):
    if request.method == 'POST':
        logout(request.POST)
        return redirect(index)
    else:
        return redirect(connexion)


def erreur(request,name):
    return render(request, 'Enigmes/maenigme.html', {'question': name})


def inscription(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username_u=request.POST.get('username')
            try:
                user = User.objects.get(username=username_u)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'), password=request.POST['password'],email=request.POST['email'])
                user.save()
                user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                login(request, user)
                return redirect(index)
            return HttpResponse("Vous existez deja petit bigorneau!")
            
        else:
            return HttpResponse("erreur formulaire invalide")
    else:
        form = RegisterForm()
    return render(request, 'Enigmes/inscription.html', {'form': form})

#def inscription(request):
#return render(request, 'Enigmes/formulaire.html',locals())


def jouer(request):
    return render(request, 'Enigmes/vide.html')