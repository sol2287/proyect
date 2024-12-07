from django.db import models

# Create your models here.

# Tablas Animales
class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=150)
    color= models.CharField(max_length=10)
    fecha= models.DateField()
#Tabla caninos
class Caninos(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=150)
    color= models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha= models.DateField()

