#libreries
from hospitalApp.models.historiaClinica import HistoriaClinica
from rest_framework import serializers

#creacion de clase para serializarla
class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['oximetria','f_respiratoria','f_cardiaca','temperatura','presionArterial','glicemias','diagnostico','sugerencia'] #atributos o campos que necesitamos serializar.
