from django.shortcuts import render
from django.http import HttpResponse
from vacuna_maule.models import Vacuna

# Create your views here.

def index(request):
    return render(request, "index.html")

def ingresar(request):
    return render(request, "ingresar.html")

def ingresar_vacuna(request):
    if request.method == 'GET':
        nombre = request.GET['txt_nombre']
        appaterno = request.GET['txt_appaterno']
        apmaterno = request.GET['txt_apmaterno']
        rut = request.GET['txt_rut']
        edad = request.GET['txt_edad']
        nombrevacuna = request.GET['txt_nombrevacuna']
        fecha = request.GET['txt_fecha']
        vacuna = Vacuna(nombre=nombre, appaterno=appaterno, apmaterno=apmaterno, rut=rut, edad=edad, nombrevacuna=nombrevacuna, fecha=fecha)
        vacuna.save()
        return render(request, "ingresar.html")
    else:
        return render(request, "ingresar.html")

def listar(request):
    vacunas = Vacuna.objects.all()
    return render(request, "listar.html", {'vacunas': vacunas})

def listar_pagina(request):
    return render(request, "listar.html")

def buscar(request):
    return render(request, "buscar.html")

def buscador(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        info = Vacuna.objects.filter(rut__icontains=persona)
        return render(request,"ingreso_buscar.html",{"query":persona, "info":info})
    else:
        msg = "<h1>Ingrese Rut Valido</h1>"
        return HttpResponse(msg)