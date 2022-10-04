# librerias
from django.db import models 
#creando la referencia / relacion que hay entre user y account 1:1
from .user   import User

#Clase del modelo de la cuenta
class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='medico',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    especialidad = models.CharField('especialidad', max_length=50)