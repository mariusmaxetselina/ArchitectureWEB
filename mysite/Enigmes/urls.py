#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),#, name='index' a jouter en paramètre pour utiliser une variable textuelle et l'afficher telle quel
    url(r'^Accueil$', views.index),
    url(r'^connexion', views.connexion),
    url(r'^Enigmes', views.jouer),
    url(r'^devinettej', views.devinettejoueur),
    url(r'^inscription', views.inscription, name='inscription'),
    url(r'^devinette/(?P<titreQ>[0-9]+)/$', views.list_enigmes),
    url(r'^deconnexion', views.deconnexion),
]
"""pour articleS, ici c'est la création de variables et leur nombre de
 digit qui est important"""