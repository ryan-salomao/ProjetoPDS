from django import forms
from app.models import Usuario
from app.models import Funcionario

# Create the form class.
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'senha']
        widgets = {
            'senha': forms.PasswordInput, 
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['atendimento', 'pontualidade', 'qualidade']
