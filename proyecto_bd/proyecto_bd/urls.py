"""proyecto_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vacuna_maule import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('ingresar/', views.ingresar),
    path('ingresar_vacuna/', views.ingresar_vacuna),
    path('listar/', views.listar),
    path('buscar/', views.buscar),
    path('listar_pagina/', views.listar_pagina),
    path('buscador/', views.buscador),
    path('ingresar_trabajador/', views.ingresar_trabajador),
    path('listar_trabajador/', views.listar_trabajador),
    path('listar_trabajador_lista/', views.listar_trabajador_lista),
    path('ingresar_trabajador_lista/', views.ingresar_trabajador_lista),
    path('actualizar_trabajador/', views.actualizar_trabajador),
    path('actualizar_trabajador_lista/', views.actualizar_trabajador_lista),
    path('eliminar_trabajador/', views.eliminar_trabajador),
    path('eliminacion_trabajador/', views.eliminacion_trabajador),
    path('buscador_trabajador/', views.buscador_trabajador),
    path('buscar_ingreso_trabajador/', views.buscar_ingreso_trabajador),
]

urlpatterns += staticfiles_urlpatterns()