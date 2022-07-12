from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=40)
    appaterno = models.CharField(max_length=40)
    apmaterno = models.CharField(max_length=40)
    rut = models.CharField(max_length=10)
    edad = models.CharField(max_length=3)
    nombrevacuna = models.CharField(max_length=40)
    fecha = models.DateField()

class Trabajador(models.Model):
    nombre = models.CharField(max_length=40)
    appaterno = models.CharField(max_length=40)
    apmaterno = models.CharField(max_length=40)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
