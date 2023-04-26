from django.forms import ModelForm
from app.models import Usuario
from app.models import Funcionario

# Create the form class.
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'senha']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['atendimento', 'pontualidade', 'qualidade']
