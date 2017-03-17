#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django import forms

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

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
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(deconnexion)
            else:
                messages.add_message(request, messages.ERROR, "Erreur de mot de passe ou de nom d'utilisateur")
                return redirect(index)
    else:
        formLogin = LoginForm()
    formRegister = RegisterForm()
    return render(request, 'Enigmes/connexion.html', {'formRegister': formRegister, 'formLogin': formLogin})

def deconnexion(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Vous avez été correctement deconnecté! A bientôt ! ")
        return redirect(index)
    else:
        if not request.user.is_authenticated:
            return redirect(connexion)
        else:
            return render(request, 'Enigmes/connexion.html')

def inscription(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username_u=request.POST['username']
            try:
                user = User.objects.get(username=username_u)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'), password=request.POST['password'],email=request.POST['email'])
                user.save()
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                messages.success(request, "Vous êtes à présent inscrit!")
                return redirect(deconnexion)
            messages.add_message(request, messages.ERROR, "Erreur ce pseudo correspond déjà à un profil existant!")
            return redirect(index)
        else:
            messages.add_message(request, messages.ERROR, "Erreur formulaire!")
            return redirect(index)
    else:
        form = RegisterForm()
    return render(request, 'Enigmes/inscription.html', {'form': form})

#def inscription(request):
#return render(request, 'Enigmes/formulaire.html',locals())


def jouer(request):
    return render(request, 'Enigmes/vide.html')