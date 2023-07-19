from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import Usuario
from app.forms import FuncionarioForm
from app.models import Atendimento
from app.geolocalizacao import buscar_distancias
from app.favoritos import favoritar_usuario, remover_usuario, lista_favoritos

def home(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = UsuarioForm()
    return render(request, 'form.html', data)

def pesquisa_result(request):
    data = {}
    data['db'] = Atendimento.objects.all()
    return render(request, 'pesquisa_result.html', data)

def createuser(request):
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)

def pesquisas(request):
    data = {}
    data['db'] = Atendimento.objects.all()
    return render(request, 'pesquisa_result.html', data)

def pesquisa(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'pesquisa.html', data)

def geo(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'geo.html', data)

def geo_result(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        raise Http404("Usuário não existe")
    
    enderecos_banco = []
    distancias = []
    queryset = Usuario.objects.all()

    for user in queryset:
        enderecos_banco.append(user.endereco)

    distancias = buscar_distancias(usuario.endereco, enderecos_banco)

    context = {
        'usuario': usuario,
        'distancias': distancias,
    }
    return render(request, "geo_result.html", context)

def favoritar(user, pk):
    favoritar_usuario(Usuario.objects.get(pk=pk))

    return redirect('home')

def desfavoritar(user, pk):
    remover_usuario(Usuario.objects.get(pk=pk))

    return redirect('favoritos')

def favoritos(request):
    funcionarios = lista_favoritos()

    context = {
        'funcionarios': funcionarios, 
    }
    return render(request, 'favoritos.html', context)

def filtro(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'filtro.html', data)

def feedback_user(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'feedback_user.html', data)

def create(request):
    form = FuncionarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')