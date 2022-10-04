#libreries
from hospitalApp.models.paciente import Paciente
from rest_framework import serializers

#creacion de clase para serializarla
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['medicoId','hisCliId','enfermeroId'] #atributos o campos que necesitamos serializar.
