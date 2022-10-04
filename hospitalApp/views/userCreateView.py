from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalApp.serializers.userSerializer import UserSerializer
from hospitalApp.models.user import User
from hospitalApp.serializers.userSerializer import EditUserSerializer

# creamos un nuevo usuario usando una clase 

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class UserEditview(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = EditUserSerializer

    def Update(self, request, *args, **kwargs):
        data_to_change = {'nombre': request.data.get("nombre")}
        # Partial update of the data
        serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

        return Response(serializer.data)





