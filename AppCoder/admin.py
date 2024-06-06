from django.contrib import admin
from .models import Curso, Profesores, Estudiantes, Entregable

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre',"camada"]
    search_fields = ['nombre',"camada"]
    list_filter = ['nombre']

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesores)
admin.site.register(Estudiantes)
admin.site.register(Entregable)