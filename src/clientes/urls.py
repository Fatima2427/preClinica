
from django.conf.urls import url, include
from clientes.views import (index, register,eleccion, login, logout, base, perfiles, )
from clientes.views import imprimir
from django.urls import include, path
urlpatterns = [
    url(r'^$', index ,name ='index'),
    url(r'^register', register, name ='register'),
    url(r'^login', login, name='login'),
    url(r'^logout/',logout,name='logout'),
    url(r'^base',base,name='base'),
    path('perfiles/',perfiles,name='perfiles'),
    url(r'^mi_pdf/$', imprimir.as_view(), name='mi_pdf'),
    url(r'^eleccion/', eleccion, name='eleccion'),
    ]