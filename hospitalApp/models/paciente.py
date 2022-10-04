# librerias
from django.db import models

#creando la referencia / relacion que hay entre user y account 1:1
from .user import User
from .medico import Medico
from .historiaClinica import HistoriaClinica
from .enfermeroPaciente import EnfermeroPaciente

#Clase del modelo de la cuenta
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='paciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    medicoId = models.ForeignKey(Medico, related_name='paciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    hisCliId = models.ForeignKey(HistoriaClinica, related_name='paciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    enfermeroId = models.ForeignKey(EnfermeroPaciente, related_name='paciente',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
