from django.conf.urls import url, include
from medicos.views import (logeoMedico,registroMedic, MedicoRuta, mostrar)
from django.urls import include, path
urlpatterns = [
    url(r'^logeoMedico', logeoMedico, name='logeo'),
    url(r'^MedicoRuta',MedicoRuta,name='rutaMedico'),
    url(r'^mostrar',mostrar,name='pacientes'),
    url(r'^registroMedic/', registroMedic, name='Medic'),
    ]