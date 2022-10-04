# librerias
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    """
    Funcion para crear un usuario
    self: es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase.
    """
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # funcion que permite crear superUsuario
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user( 
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """
    Creacion de la clase usuario
    """
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField ('user_type', max_length = 20)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    email = models.EmailField('Email', max_length = 100)
    nombre = models.CharField('nombre', max_length = 30)
    apellido = models.CharField('apellido', max_length = 30)
    direccion = models.CharField('direccion', max_length = 30)

    def save(self, **kwargs): #argumentos arbitrarios
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs) #funcion save para guardar los datos ya que se esta encriptando la contrasena

    objects = UserManager()
    USERNAME_FIELD = 'username'   
