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
from .models import Enigmes,Joueur

def index(request):
    return render(request, 'Enigmes/accueil.html',locals())


def list_enigmes(request, titreQ):
    try:
        rock = Enigmes.objects.get(numero=titreQ)
    except Enigmes.DoesNotExist:
        raise Http404("Globiboulga")
    return render(request, 'Enigmes/maenigme.html', {'question': rock})  #pour tester sans etre connecte
    #return render(request, 'Enigmes/enigmes.html', {'question': rock})  #pour tester en etant connecte
    #Il faut se connecter 
    # Aller sur http://127.0.0.1:8000/devinette/X avec X le numero de l'enigme


def connexion(request):
    if request.method == 'POST':
    	form = LoginForm(request.POST)
    	if form.is_valid():
    		username_u=request.POST.get('username')
    		password_p=request.POST.get('password')
        user = authenticate(username=username_u,password=password_p)
        if user is not None:
        	login(request, user)
          	#return HttpResponse("Vous existez petit bigorneau!")
          	return redirect(index)
        else:
            return HttpResponse("utilisateur inconnu")
    else:
    	#user = authenticate(username='Elliot', password='moi')
        #login(request, user)
        #return redirect(index)
        form = LoginForm()
        formRegister = RegisterForm()
        return render(request, 'Enigmes/connexion.html', {'formRegister': formRegister, 'form': form})


def deconnexion(request):
    logout(request)
    return redirect(index)

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
                joueur = Joueur()
                joueur.level=1
                joueur.master=False
                joueur.user=user
                joueur.save()
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
    return render(request, 'Enigmes/enigmes.html')


def devinettejoueur(request):
    return render(request, 'Enigmes/vide.html')

def psuivante(request, nombre1):    
    total = int(nombre1) + 1
    return render(request, 'polls/addition.html', locals())




