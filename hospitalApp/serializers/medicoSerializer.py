#libreries
from hospitalApp.models.medico import Medico
from rest_framework import serializers

#creacion de clase para serializarla
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['especialidad'] #atributos o campos que necesitamos serializar.
