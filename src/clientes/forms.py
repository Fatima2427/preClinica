from django import forms
from django.contrib.auth.models import User
from .models import Paciente

class FormPaciente(forms.ModelForm):
    class Meta:
        model=Paciente
        fields=('dni', 'genero', 'fecha_nacimiento', 'edad', 'telefono', 'direccion','doctor', 'alergias', 'enfermedades', 'medicamentos')

