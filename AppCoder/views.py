from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario

# Create your views here.

def curso(req, nombre, camada):

    nuevo_curso = Curso(nombre=nombre, camada = camada)
    nuevo_curso.save()

    return HttpResponse
    (f"""
     <p>Curso:{nuevo_curso.nombre} - Camada{nuevo_curso.camada} creado!</p>                       
     """)

def lista_cursos(req):

    lista = Curso.objects.all() 
    return render(req, 'lista_cursos.html', {'lista': lista})

def inicio(req):
    return render(req, "inicio.html", {})

def cursos(req):
    return render(req, "cursos.html", {})

def profesores(req):
    return render(req, "profesores.html", {})

def estudiantes(req):
    return render(req, "estudiantes.html", {})

def entregables(req):
    return render(req, "entregables.html", {})

def curso_formulario (req):

     print('method: ' ,req.method)
     print('POST: ' ,req.POST)
     if req.method == 'POST':
      
      miformulario = CursoFormulario(req.POST)

      print(miformulario)

      if miformulario.is_valid():
       
       data = miformulario.cleaned_data

       nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
       nuevo_curso.save()
       return render(req,"Inicio.html", {"messge":"Curso creado con exito"} )
      else:
         return render(req,"Inicio.html", {"messge":"Datos invalidos"} )

     else:
      
      miformulario = CursoFormulario()

      return render(req, "curso_formulario.html", {"miformulario" : miformulario}) 
    

def busqueda_camada(req):
   return render(req,"busqueda_camada.html",{})

def buscar(req):
   
   if req.GET["camda"]:
      
      camada = req.GET["camada"]

      cursos = Curso.objects.filter(camada__icontains=camada)
      
      return render(req,"resultadoBusqueda.html", {"cursos": cursos, "camada": camada} )
   
   else:
      
      return render(req,"Inicio.html", {"messge":"no envias el dato de la camada"} )


   