from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField(null=True)
    
    
class Profesores(models.Model):
    camada = models.IntegerField(Curso)  
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
