#importando librerias
from rest_framework import serializers

#libreria
#relacionando modelos
from hospitalApp.models.user import User
from hospitalApp.models.medico import Medico
from hospitalApp.models.paciente import Paciente
from hospitalApp.models.userGeneral import UserGeneral
from hospitalApp.models.familiar import Familiar
from hospitalApp.serializers.medicoSerializer import MedicoSerializer
from hospitalApp.serializers.userGeneralSerializer import UserGeneralSerializer
from hospitalApp.serializers.pacienteSerializer import PacienteSerializer
from hospitalApp.serializers.familiarSerializer import FamiliarSerializer


class UserSerializer(serializers.ModelSerializer): 
    userGeneral = UserGeneralSerializer()
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'nombre', 'apellido', 'direccion']
        # , 'userGeneral'

    #convertir los modelos en un formato JSON y de JSON a modelo
    #funcion que crea al mismo tiempo usuario y cuenta (donde se visualiza como un solo prooceso del lado del cliente)
    def create(self, validated_data):
        # userGeneralData = validated_data.pop('userGeneral')
        userInstance = User.objects.create(**validated_data)
        # UserGeneral.objects.create(user=userInstance, **userGeneralData)
        return userInstance        
    
    #La funcion hace es sobreescribe el metodo para obtener usuario y cuenta en uno solo (obtener los dos obtejos usuario y la cuenta - representados por dos modelos - ORM)
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        # userGeneral = UserGeneral.objects.get(user=obj.id)
        return {
                'id': user.id,
                'user_type': user.user_type,
                'username': user.username,
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'direccion': user.direccion,
                # 'userGeneral':{
                #     'id':userGeneral.id,
                #     'area': userGeneral.area,
                #     'auxiliar': userGeneral.auxiliar
                # }
            }

class EditUserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ('nombre',)

   def update(self, instance, validated_data): 
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance



class MedicoSerializer(serializers.ModelSerializer): 
    medico = MedicoSerializer()
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'nombre', 'apellido', 'direccion', 'medico']

    #convertir los modelos en un formato JSON y de JSON a modelo
    #funcion que crea al mismo tiempo usuario y cuenta (donde se visualiza como un solo prooceso del lado del cliente)
    def create(self, validated_data):
        medicoData = validated_data.pop('medico')
        userInstance = User.objects.create(**validated_data)
        Medico.objects.create(user=userInstance, **medicoData)
        return userInstance
    
    #La funcion hace es sobreescribe el metodo para obtener usuario y cuenta en uno solo (obtener los dos obtejos usuario y la cuenta - representados por dos modelos - ORM)
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        medico = Medico.objects.get(user=obj.id)
        return {
                'id': user.id,
                'user_type': user.user_type,
                'username': user.username,
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'direccion': user.direccion,
                'medico':{
                    'id':medico.id,
                    'especialidad': medico.especialidad
                }
            }

class PacienteSerializer(serializers.ModelSerializer): 
    paciente = PacienteSerializer()
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'nombre', 'apellido', 'direccion', 'paciente']

    #convertir los modelos en un formato JSON y de JSON a modelo
    #funcion que crea al mismo tiempo usuario y cuenta (donde se visualiza como un solo prooceso del lado del cliente)
    def create(self, validated_data):
        pacienteData = validated_data.pop('paciente')
        userInstance = User.objects.create(**validated_data)
        Paciente.objects.create(user=userInstance, **pacienteData)
        return userInstance
    
    #La funcion hace es sobreescribe el metodo para obtener usuario y cuenta en uno solo (obtener los dos obtejos usuario y la cuenta - representados por dos modelos - ORM)
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        paciente = Paciente.objects.get(user=obj.id)
        return {
                'id': user.id,
                'user_type': user.user_type,
                'username': user.username,
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'direccion': user.direccion,
                'paciente':{
                    'id':paciente.id,
                    'medicoId': paciente.id,
                    'hisCliId': paciente.id,
                    'enfermeroId':paciente.id
                    }
                }
                    
class FamiliarSerializer(serializers.ModelSerializer): 
    familiar = FamiliarSerializer()
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'nombre', 'apellido', 'direccion', 'familiar']

    #convertir los modelos en un formato JSON y de JSON a modelo
    #funcion que crea al mismo tiempo usuario y cuenta (donde se visualiza como un solo prooceso del lado del cliente)
    def create(self, validated_data):
        userGeneralData = validated_data.pop('familiar')
        userInstance = User.objects.create(**validated_data)
        Familiar.objects.create(user=userInstance, **userGeneralData)
        return userInstance
    
    #La funcion hace es sobreescribe el metodo para obtener usuario y cuenta en uno solo (obtener los dos obtejos usuario y la cuenta - representados por dos modelos - ORM)
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        familiar = Familiar.objects.get(user=obj.id)
        return {
                'id': user.id,
                'user_type': user.user_type,
                'username': user.username,
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'direccion': user.direccion,
                'familiar':{
                    'id':familiar.id,
                    'parentesco': familiar.parentesco
                }
            }            