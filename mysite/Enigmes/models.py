#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Enigmes(models.Model):

    question = models.CharField(max_length=1000)

    reponse = models.CharField(max_length=50)

    numero = models.IntegerField()

    auteur = models.CharField(max_length=20)
    

    def __str__(self):

        return self.question

class Joueur(models.Model):

    Pseudo = models.CharField(max_length=20)

    password = models.CharField(max_length=50)

    level = models.IntegerField()

    email = models.EmailField(max_length=40)

    master = models.BooleanField()

    def __str__(self):

        return self.adr

