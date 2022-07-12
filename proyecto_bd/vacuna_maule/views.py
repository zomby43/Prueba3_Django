from django.shortcuts import render
from django.http import HttpResponse
from vacuna_maule.models import Vacuna
from vacuna_maule.models import Trabajador

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

def listar_trabajador_lista(request):
    trabajadores = Trabajador.objects.all()
    return render(request, "listar_trabajador.html", {'trabajadores': trabajadores})

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

def ingresar_trabajador(request):
    return render(request, "ingresar_trabajador.html")

def listar_trabajador(request):
    return render(request, "listar_trabajador.html")

def ingresar_trabajador_lista(request):
    if request.method == 'GET':
        nombre = request.GET['txt_t_nombre']
        appaterno = request.GET['txt_t_appaterno']
        apmaterno = request.GET['txt_t_apmaterno']
        rut = request.GET['txt_t_rut']
        telefono = request.GET['txt_t_telefono']
        trabajador = Trabajador(nombre=nombre, appaterno=appaterno, apmaterno=apmaterno, rut=rut, telefono=telefono)
        trabajador.save()
        mensaje = "Trabajador Guardado"
    else:
        mensaje = "Trabajador No Guardado"
    return HttpResponse(mensaje+"<a href='/index/'>Volver</a>")

def actualizar_trabajador(request):
    return render(request, "actualizar_trabajador.html")

def actualizar_trabajador_lista(request):
    if request.GET["txt_t_rut"]:
        rut_recibido = request.GET["txt_t_rut"]
        telefono_recibido = request.GET["txt_t_telefono"]
        trabajador = Trabajador.objects.filter(rut=rut_recibido)
        if trabajador:
            info = Trabajador.objects.get(rut=rut_recibido)
            info.telefono = telefono_recibido
            info.save()
            mensaje = "Trabajador Actualizado"
        else:
            mensaje = "Trabajador No Actualizado"
    else:
        mensaje = "Debe ingresar un rut para actualizar."
    return HttpResponse(mensaje+"<a href='/index/'>Volver</a>")

def eliminar_trabajador(request):
    return render(request, "eliminar_trabajador.html")

def buscar_trabajador(request):
    return render(request, "buscar_trabajador.html")

def eliminacion_trabajador(request):
    if request.GET["txt_t_id"]:
        id_recibido = request.GET["txt_t_id"]
        trabajador = Trabajador.objects.filter(id=id_recibido)
        if trabajador:
            info = Trabajador.objects.get(id=id_recibido)
            info.delete()
            mensaje="<h2>Trabajador Eliminado</h2>"
        else:
            mensaje="<h2>No se pudo eliminar al trabajador</h2>"
    else:
        mensaje="<h2>Debe ingresar un id para eliminar....</h2>"
    return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver</h2>")

def buscador_trabajador(request):
    if request.GET["txt_t_id"]:
        persona_trabajador = request.GET["txt_t_id"]
        info_trabajador = Trabajador.objects.filter(id__icontains=persona_trabajador)
        return render(request,"buscar_trabajador.html",{"query_trab":persona_trabajador, "info_trabajador":info_trabajador})
    else:
        msg = "<h1>Ingrese ID Valido</h1>"
        return HttpResponse(msg)

def buscar_ingreso_trabajador(request):
    return render(request, "buscar_ingreso_trabajador.html")