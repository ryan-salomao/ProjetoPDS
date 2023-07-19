from django.contrib import admin
from .models import Usuario, Atendimento, Funcionario, Categoria



class AtendimentoAdmin(admin.ModelAdmin):
    list_display = [
        "funcionario", 
        "atendimento",
        "qualidade",
        "pontualidade",
    ]

    list_filter = [
        "funcionario", 
        "atendimento",
        "qualidade",
        "pontualidade",
    ]

admin.site.register(Atendimento, AtendimentoAdmin)

admin.site.register(Usuario)

class FuncionarioAdmin(admin.ModelAdmin):
    filter_horizontal = [
        "categorias",
    ]

admin.site.register(Funcionario, FuncionarioAdmin)

admin.site.register(Categoria)