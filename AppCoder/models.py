from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"
    
    class Meta():
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ("nombre","camada")
        unique_together = ("nombre","camada")
    
    
class Profesores(models.Model):
    camada = models.IntegerField(Curso)  
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    profesion = models.CharField(max_length=30)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)