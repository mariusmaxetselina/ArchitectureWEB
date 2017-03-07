#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),#, name='index' a jouter en paramètre pour utiliser une variable textuelle et l'afficher telle quel
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/', views.addition),
    url(r'^article/(\d+)', views.view_article),  # Vue d'un article le nombre de digit est infini
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),
    url(r'^connexion', views.connexion),
    url(r'^date$', views.date_actuelle),
    url(r'^Enigmes', views.jouer),
    url(r'^inscription', views.inscription),
]
"""pour articleS, ici c'est la création de variables et leur nombre de
 digit qui est important"""