from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Answer(models.Model):
    answ = models.CharField(max_length=50)

    def __str__(self):
        return self.answ

class Malumot(models.Model):
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.data

class User(models.Model):
    fullname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname

