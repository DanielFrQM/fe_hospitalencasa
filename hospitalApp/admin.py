from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.medico import Medico
from . models.familiar import Familiar
from .models.enfermeroPaciente import EnfermeroPaciente
from .models.paciente import Paciente
# from .models.userGeneral import UserGeneral

admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Familiar)
admin.site.register(Paciente)
admin.site.register(EnfermeroPaciente)

# admin.site.register(userGeneral)


