from django import forms
from .models import Paciente, Medico
from django.contrib.auth.models import User
from .models import Paciente, Medico


class FormPaciente(forms.ModelForm):
    class Meta:
        model=Paciente
        fields=('dni', 'genero', 'fecha_nacimiento', 'edad', 'telefono', 'direccion', 'alergias', 'enfermedades', 'medicamentos')

class FormMedico(forms.ModelForm):
    class Meta:
        model=Medico
        fields=('dni', 'img', 'genero', 'fecha_nacimiento', 'edad', 'telefono', 'direccion', 'titulo', 'especialidad')
        