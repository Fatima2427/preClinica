from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import FormPaciente
from medicos.forms import FormMedico
from clientes.models import Paciente
from medicos.models import Doctor
from django.views.generic import View
from clinica.utileria import render_pdf
from django.http import HttpResponse
from clinica.utileria import render_pdf
from django.shortcuts import render
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def logeoMedico(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user= auth.authenticate(username=username,password=password) 
		if user is not None:
			auth.login(request, user)
			return redirect('MedicoRuta')
			
		else:
			messages.info(request,'invalid credentials')
			print('fallo datos')
			return redirect('logeoMedico')
			
	else:
		return render(request, 'clientes/logeo.html')
def registroMedic(request):
	medico_form=FormMedico()
	if request.method =='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		medico_form=FormMedico(request.POST)

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
				print('falso')
				return redirect('registroMedic')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'email taken')
				print('repetido')
				return redirect('registroMedic')
			else:
				if medico_form.is_valid():
					user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
					profile=medico_form.save(commit=False)
					profile.user=user
					profile.save()
					user.save()
					print('user created')
					return redirect('logeoMedico')
		
		else:
			print('password not maching..')
			return redirect('registroMedic')
		return redirect('/')
	else:
		context={'medico_form':medico_form}
		return render(request, 'clientes/Medic.html', context)


def MedicoRuta(request):
	return render(request, 'clientes/rutaMedico.html')
def mostrar	(request):

	medico =Paciente.objects.all()
	
	return render(request , 'clientes/pacientes.html', {'medico' : medico})