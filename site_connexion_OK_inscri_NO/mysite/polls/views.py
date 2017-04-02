#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from django.shortcuts import render

def index(request):
    return render(request, 'polls/accueil.html',locals())

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
    return render(request, 'polls/date.html',locals())



def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)


    # Retourne nombre1, nombre2 et la somme des deux au tpl

    return render(request, 'polls/addition.html', locals())