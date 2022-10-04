from hospitalApp.models.enfermeroPaciente import EnfermeroPaciente
from hospitalApp.serializers.enfermeroPacienteSerializer import EnfermeroPacienteSerializer
from hospitalApp.models.userGeneral import UserGeneral
from rest_framework import serializers

#creacion de clase para serializarla
class UserGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeneral
        fields = ['area', 'auxiliar'] #atributos o campos que necesitamos serializar.


class EnfermeroPacienteSerializer(serializers.ModelSerializer): 
    EnfermeroPaciente = EnfermeroPacienteSerializer()
    class Meta:
        model = UserGeneral
        fields = ['id', 'user', 'area', 'auxiliar', 'EnfermeroPaciente']

    #convertir los modelos en un formato JSON y de JSON a modelo
    #funcion que crea al mismo tiempo usuario y cuenta (donde se visualiza como un solo prooceso del lado del cliente)
    def create(self, validated_data):
        enfermeroData = validated_data.pop('enfermeroPaciente')
        userInstance = UserGeneral.objects.create(**validated_data)
        EnfermeroPaciente.objects.create(user=userInstance, **enfermeroData)
        return userInstance
    
    #La funcion hace es sobreescribe el metodo para obtener usuario y cuenta en uno solo (obtener los dos obtejos usuario y la cuenta - representados por dos modelos - ORM)
    def to_representation(self, obj):
        UserGeneral = UserGeneral.objects.get(id=obj.id)
        EnfermeroPaciente = EnfermeroPaciente.objects.get(user=obj.id)
        return {
                'id': UserGeneral.id,
                'area': UserGeneral.area,
                'auxiliar': UserGeneral.auxiliar,
                'EnfermeroPaciente':{
                    'id':EnfermeroPaciente.id,
                    'citaDate': EnfermeroPaciente.citaDate,
                    'notas': EnfermeroPaciente.notas,
                    }
                }