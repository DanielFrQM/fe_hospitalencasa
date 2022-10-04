# librerias
from django.db import models 
#creando la referencia / relacion que hay entre user y account 1:1

#Clase del modelo de la cuenta
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.CharField('oximetria', max_length=45)
    f_respiratoria = models.IntegerField(default=0) 
    f_cardiaca = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    presionArterial = models.IntegerField(default=0)
    glicemias = models.IntegerField(default=0)
    diagnostico = models.CharField('diagnostico', max_length = 100)
    sugerencia = models.CharField('sugerencia', max_length =100)