#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from django.shortcuts import render

def index(request):

    return HttpResponse("Ouais c'est l'accueil. T'as un problème avec ça?")