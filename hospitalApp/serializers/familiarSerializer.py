from hospitalApp.models.familiar import Familiar
from rest_framework import serializers

#creacion de clase para serializarla
class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['parentesco'] #atributos o campos que necesitamos serializar.
