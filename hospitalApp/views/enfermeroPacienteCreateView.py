from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalApp.serializers.enfermeroPacienteSerializer import EnfermeroPacienteSerializer

# creamos un nuevo usuario usando una clase 

class EnfermeroPacienteCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = EnfermeroPacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



