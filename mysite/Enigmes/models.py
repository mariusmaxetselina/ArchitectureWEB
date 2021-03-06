#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Enigmes(models.Model):
	
    question = models.CharField(max_length=1000)

    reponse = models.CharField(max_length=50)

    numero = models.IntegerField()

    auteur = models.CharField(max_length=20)
    

    def retQ(self):

        return self.question

class Joueur(models.Model):

    user = models.OneToOneField(User)

    level = models.IntegerField()

    master = models.BooleanField()