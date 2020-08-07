
from django.conf.urls import url, include
from clientes.views import (index, register,mostrar,eleccion,contacto, login, logeoMedico, logout, base, perfiles, registroMedic, MedicoRuta)
from clientes.views import imprimir
from django.urls import include, path
urlpatterns = [
    url(r'^$', index ,name ='index'),
    url(r'^register', register, name ='register'),
    url(r'^login', login, name='login'),
    url(r'^logeoMedico', logeoMedico, name='logeo'),
    url(r'^logout/',logout,name='logout'),
    url(r'^base',base,name='base'),
    url(r'^MedicoRuta',MedicoRuta,name='rutaMedico'),
    url(r'^mostrar',mostrar,name='pacientes'),
    path('perfiles/',perfiles,name='perfiles'),
    url(r'^mi_pdf/$', imprimir.as_view(), name='mi_pdf'),
    url(r'^registroMedic/', registroMedic, name='Medic'),
    url(r'^eleccion/', eleccion, name='eleccion'),
    url(r'^contacto/', contacto, name='contacto'),
    ]