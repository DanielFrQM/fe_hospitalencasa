# librerias
from django.db import models 
#creando la referencia / relacion que hay entre user y account 1:1
# from .paciente   import Paciente
from .userGeneral import UserGeneral

#Clase del modelo de la cuenta
class EnfermeroPaciente(models.Model):
    id = models.AutoField(primary_key=True)
    auxiliarId = models.ForeignKey(UserGeneral, related_name='enfermeroPaciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    # pacienteId = models.ForeignKey(Paciente, related_name='enfermeroPaciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    citaDate = models.DateTimeField()
    notas = models.CharField('notas', max_length=100)
