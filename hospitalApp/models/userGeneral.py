# librerias
from django.db import models 
#creando la referencia / relacion que hay entre user y account 1:1
from .user import User

class UserGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='userGeneral', on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK
    area = models.CharField('area', max_length=50)
    auxiliar = models.BooleanField(default=True)