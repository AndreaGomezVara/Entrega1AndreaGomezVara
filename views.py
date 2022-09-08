from curses.ascii import HT
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

def Usuario (request):
    return render(request,"AppCoder/Usuario.html")

def Juegos (request):
    return render(request,"AppCoder/Juegos.html")

def Personajes(request):
    return render(request,"AppCoder/Personajes.html")

def Inicio (request):
    return render(request,"AppCoder/Inicio.html")

def JuegosFormulario(request):
    if request.method == 'POST':
        miFormulario= JuegosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleanead_data
            juego= Juegos (nombre=informacion['nombre'], genero=informacion['genero'])
            juego.save()
        return render (request, "AppCoder/inicio.html")
    
    else:
        miFormulario=  JuegosFormulario()

    return render (request, "AppCoder/Formulario.html", {'miFormulario': miFormulario})


def BusquedaJuegos(request):
    return render(request, "AppCoder/Busqueda.html")

def buscar(request):

    if request.GET ["nombre"]:
      nombre= request.GET ["nombre"]
      juegos= Juegos.objects.filter(camada__icontains=nombre)  
    
    return render(request, "AppCoder/buscar")




