from .models import Usuario

favoritos = []

def favoritar_usuario(usuario):
    favoritos.append(usuario)

def remover_usuario(usuario):
    favoritos.remove(usuario)

def lista_favoritos():
    return favoritos

# será feito na model Usuario