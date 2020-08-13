from django import forms
from django.contrib.auth.models import User
from .models import Doctor
class FormMedico(forms.ModelForm):
    class Meta:
        model= Doctor
        fields=('dni', 'img', 'genero', 'fecha_nacimiento', 'edad', 'telefono', 'direccion', 'titulo', 'especialidad')
        