from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppNomads.models import Curso, Nomade
from AppNomads.forms import CursoFormulario, NomadesFormulario

# Create your views here.

def curso(request):

      curso  =  Curso(nombre="Curso Freelance", codigo="1")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Codigo: {curso.codigo}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppNomads/inicio.html")



def usuarios(request):

      return render(request, "AppNomads/usuarios.html")


def viajes(request):

      return render(request, "AppNomads/viajes.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí me llega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], codigo=informacion['codigo']) 

                  curso.save()

                  return render(request, "AppNomads/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppNomads/cursos.html", {"miFormulario":miFormulario})




def nomades(request):

      if request.method == 'POST':

            miFormulario = NomadesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  nomade = Nomade (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  nomade.save()

                  return render(request, "AppNomads/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= NomadesFormulario() #Formulario vacio para construir el html

      return render(request, "AppNomads/nomades.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["codigo"]:

	      #respuesta = f"Estoy buscando el codigo nro: {request.GET['codigo'] }" 
            codigo = request.GET['codigo'] 
            cursos = Curso.objects.filter(codigo__icontains=codigo)

            return render(request, "AppNomads/inicio.html", {"cursos":cursos, "codigo":codigo})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)


      