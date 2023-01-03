from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models. Model):
    nume =models. CharField(max_length=100)
    prenume =models. CharField(max_length=100)
    email =models. CharField(max_length=100)
    numar_tel =models. IntegerField()
    sex =models. CharField(max_length=100)
    adresa =models. CharField(max_length=100)
    codpostal =models. IntegerField()
    


    def __str__(self):
        return self.nume


class AddBook (models.Model):
    author = models. CharField(max_length=200, null=False, blank=False)
    title = models. CharField (max_length=200, null=False, blank=False)
    description = models. TextField()
    def _str_(self):
        return self.title




class Inscrieri (models. Model):
    numeparinte =models. CharField(max_length=100)
    adresa =models. CharField(max_length=100)
    codpostal =models. IntegerField()
    nrtel =models. IntegerField()
    email =models. CharField(max_length=100)
    cnpparinte =models. IntegerField()
    numecopil =models. CharField(max_length=100)
    initiala=models.CharField(max_length=100)
    cnpcopil =models. IntegerField()

    def __str__(self):
        return self.numecopil
