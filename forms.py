from socket import fromshare
from django import forms

class FormularioNuevo (forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()

