#libreries
from hospitalApp.models.enfermeroPaciente import EnfermeroPaciente
from rest_framework import serializers

#creacion de clase para serializarla
class EnfermeroPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnfermeroPaciente
        fields = ['auxiliarId','citaDate','notas'] #atributos o campos que necesitamos serializar.
