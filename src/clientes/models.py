from django.db import models
from django.contrib.auth.models import User
from medicos.models import Doctor 
class Paciente(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dni=models.IntegerField()
    genero=models.CharField(max_length=10)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    edad=models.PositiveIntegerField(default=0 )
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=100)
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE , null=True)
    alergias=models.CharField(max_length=100,null=True)
    enfermedades=models.CharField(max_length=100,null=True)
    medicamentos=models.CharField(max_length=100,null=True)
    

def __str__(self):
    return "%s %s" % (self.first_name, self.last_name, self.username, self.password, self.email)


