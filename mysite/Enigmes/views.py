#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django import forms

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.shortcuts import render

def index(request):
    return render(request, 'Enigmes/accueil.html',locals())

def view_article(request, id_article):
    if int(id_article) > 100:
        return redirect("https://www.djangoproject.com")
    return HttpResponse("Vous voulez l'article #{0} !".format(id_article))
    """vous avez tenté d'ajouter la mention {1} request.GET['ref']"""

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse("Vous avez demandé les articles de la date {1} du mois numero {0}.".format(month, year))



def date_actuelle(request):
    date= datetime.now()
    return render(request, 'Enigmes/date.html',locals())

def connexion(request):
    if request.method == 'POST':
        formLogin = loginForm(request.POST)
        if formLogin.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(deconnexion)
            else:
                messages.add_message(request, messages.ERROR, "Erreur de mot de passe ou de nom d'utilisateur")
                return redirect(index)
    else:
        formLogin = loginForm()
    formRegister = registerForm()
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

class loginForm(forms.Form):
    username = forms.CharField(label='pseudo',min_length=2, max_length=100)
    password = forms.CharField(label='password',min_length=6, max_length=100, widget=forms.PasswordInput)

class registerForm(forms.Form):
    username = forms.CharField(label='pseudo', min_length=2, max_length=100)
    email = forms.EmailField(label='Email',min_length=5, max_length=100)
    password = forms.CharField(label='password',min_length=6, max_length=100, widget=forms.PasswordInput)

def inscription(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
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
        form = registerForm()
    return render(request, 'Enigmes/inscription.html', {'form': form})

#def inscription(request):
#return render(request, 'Enigmes/formulaire.html',locals())

def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)


    # Retourne nombre1, nombre2 et la somme des deux au tpl

    return render(request, 'Enigmes/addition.html', locals())

def jouer(request):
    return HttpResponse('Vous etes en train de jouer, profitez bien')