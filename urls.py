from django.urls import path
from AppCoder.views import *
from django.http import HttpResponse

urlpatterns = [
    path('Juegos/', Juegos, name="juegos"),
    path('Usuario/', Usuario, name="usuarios"),
    path('Personajes/', Personajes, name="personajes"),
    path('inicio/', Inicio, name="inicio"),
    path('Formulario/', JuegosFormulario, name="formulario"),
    path('busqueda/', BusquedaJuegos, name="BusquedaJuegos"),
    path('buscar/', buscar),

]