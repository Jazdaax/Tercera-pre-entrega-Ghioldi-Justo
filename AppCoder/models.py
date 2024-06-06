from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField(null=True)

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
    mail = models.EmailField(null=True)
    profesion = models.CharField(max_length=30, null=True)
    cursos = models.ManyToManyField(Curso)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)