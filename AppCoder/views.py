from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesores
from .forms import CursoFormulario, ProfesorFormulario

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
      
      miFormulario = CursoFormulario(req.POST)

      print(miFormulario)

      if miFormulario.is_valid():
       
       data = miFormulario.cleaned_data

       nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
       nuevo_curso.save()
       return render(req,"Inicio.html", {"messge":"Curso creado con exito"} )
      else:
         return render(req,"Inicio.html", {"messge":"Datos invalidos"} )

     else:
      
      miFormulario = CursoFormulario()

      return render(req, "curso_formulario.html", {"miFormulario" : miFormulario}) 
    

def busqueda_camada(req):
   return render(req,"busqueda_camada.html",{})

def buscar(req):
   
   if req.GET["camda"]:
      
      camada = req.GET["camada"]

      cursos = Curso.objects.filter(camada__icontains=camada)
      
      return render(req,"resultadoBusqueda.html", {"cursos": cursos, "camada": camada} )
   
   else:
      
      return render(req,"Inicio.html", {"messge":"no envias el dato de la camada"} )
   
def lista_profesores(req):
   
   mis_profesores = Profesores.objects.all()

   return render(req, "leer_profesores.html", {'profesores': mis_profesores})

def crea_profesor(req):
     if req.method == 'POST':
      
      miFormulario = ProfesorFormulario(req.POST)

      print(miFormulario)

      if miFormulario.is_valid():
       
       data = miFormulario.cleaned_data

       nuevo_profesor = Profesores(nombre=data['nombre'], apellido=data['apellido'], mail=data['mail'], profesion=data['profesion'])
       nuevo_profesor.save()
       return render(req,"Inicio.html", {"messge":"Curso creado con exito"} )
      else:
         return render(req,"Inicio.html", {"messge":"Datos invalidos"} )

     else:
      
      miFormulario = ProfesorFormulario()

      return render(req, "profesor_formulario.html", {"miFormulario" : miFormulario})  
     

def eliminar_profesor(req, id):     
   
   if req.method == "POST":
     profesor = Profesores.objects.get(id=id)
     profesor.delete()

     mis_profesores = Profesores.objects.all()

   return render(req, "leer_profesores.html", {'profesores': mis_profesores})

def editar_profesor(req, id):
   
    if req.method == 'POST':
      
      miFormulario = ProfesorFormulario(req.POST)

      print(miFormulario)

      if miFormulario.is_valid():
       
       data = miFormulario.cleaned_data

       profesor = Profesores.objects.get(id=id)

       profesor.nombre = data['nombre']
       profesor.apellido = data['apellido']
       profesor.mail = data['mail']
       profesor.profesion = data['profesion']
       
       profesor.save()

       return render(req,"Inicio.html", {"messge":"Profesor actualizado con exito"} )
      
      else:
         
         return render(req,"Inicio.html", {"messge":"Datos invalidos"} )

    else:
      
      profesor = Profesores.objects.get(id=id)
      
      miFormulario = ProfesorFormulario(initial={
         'nombre': profesor.nombre,
         'apellido': profesor.apellido,
         'mail': profesor.mail,
         'profesion': profesor.profesion,
      })

      return render(req, "editar_profesor.html", {"miFormulario" : miFormulario, "id": profesor.id})