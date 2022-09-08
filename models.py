from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    contraseña= models.CharField(max_length=40)

class Juegos(models.Model):
    nombre=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)

class Personajes(models.Model):
    nombre=models.CharField(max_length=40)
    habilidad=models.CharField(max_length=40)


