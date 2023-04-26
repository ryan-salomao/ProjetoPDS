from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import Usuario
from app.forms import FuncionarioForm
from app.models import Funcionario
from app.geolocalizacao import buscar_distancias

# Create your views here.
def home(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = UsuarioForm()
    return render(request, 'form.html', data)

def index1(request):
    data = {}
    data['db'] = Funcionario.objects.all()
    return render(request, 'index1.html', data)

def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)

def home1(request):
    data = {}
    data['db'] = Funcionario.objects.all()
    return render(request, 'index1.html', data)

def form1(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'form1.html', data)

def geo(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'geo.html', data)

def geo_result(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
        '''enderecos_banco = []
        queryset = Usuario.objects.all()

        for usuario in queryset:
            enderecos_banco.append(usuario.objects.get(endereco))

        buscar_distancias(usuario.endereco, enderecos_banco)'''

    except Usuario.DoesNotExist:
        raise Http404("Usuário não existe")
    context = {
        'usuario': usuario,
    }
    return render(request, "geo_result.html", context)

def create(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')