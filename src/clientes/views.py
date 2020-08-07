from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import FormPaciente, FormMedico
from clientes.models import Paciente, Medico
from django.views.generic import View
from clinica.utileria import render_pdf
from django.http import HttpResponse
from clinica.utileria import render_pdf
from django.shortcuts import render
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def send_email(mail):
	print('fase2')
	context={'mail':mail}
	template=get_template('clientes/correo.html')
	content =template.render(context)

	email= EmailMultiAlternatives(
		'Un correo de prueba',
		'Un rayo confuso',
		settings.EMAIL_HOST_USER,
		[mail]

		)
	email.attach_alternative(content, 'text/html')
	email.send()
	print('enviado')
	print(settings.EMAIL_HOST_USER)
	print(settings.EMAIL_HOST_PASSWORD)

def index(request):
	if request.method=='POST':
		mail=request.POST.get('mail')
		send_email(mail)
		print('Envio de Correo!')
	return render(request, 'clientes/index.html', {})
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user= auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			print('todo correcto')
			return redirect('base')
			
		else:
			messages.info(request,'invalid credentials')
			return redirect('../clientes/login')
			print('fallo datos')
	else:
		return render(request, 'clientes/login.html')
		print('fallo')
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


def register(request):
	paciente_form=FormPaciente()
	if request.method =='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		paciente_form=FormPaciente(request.POST)

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
				print('falso')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'email taken')
				print('repetido')
				return redirect('register')
			else:
				if paciente_form.is_valid():
					user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
					profile=paciente_form.save(commit=False)
					profile.user=user
					profile.save()
					user.save()
					print('user created')
					return redirect('login')
		
		else:
			print('password not maching..')
			return redirect('register')
		return redirect('/')
	else:
		context={'paciente_form':paciente_form}
		return render(request, 'clientes/register.html', context)
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

def logout(request):
	auth.logout(request)
	return render(request, '../clientes/')
def base(request):
	return render(request, 'clientes/base.html')

def MedicoRuta(request):
	return render(request, 'clientes/rutaMedico.html')
def mostrar	(request):

	medico =Paciente.objects.all()
	
	return render(request , 'clientes/pacientes.html', {'medico' : medico})
def perfiles(request):
    obj =Paciente.objects.get(user_id=6)
    context={ 'objeto': obj, }
    return render(request, 'clientes/perfil.html', context)
def eleccion(request):
	return render(request, 'clientes/eleccion.html')
def contacto(request):
	return render(request, 'clientes/contacto.html')
class imprimir(View):
	def get(self , request, *args, **kwargs):
		obj=Paciente.objects.get(user_id=6)
		context={ 'objeto': obj, }
		pdf=render_pdf('clientes/mi_pdf.html', context)
		return HttpResponse(
			pdf, content_type='application/pdf'
		)
