from django.contrib import admin
from .models import Funcionario
from .models import Usuario

admin.site.register(Funcionario)
admin.site.register(Usuario)