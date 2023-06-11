from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=50)
    senha = models.CharField(max_length=6)
    favoritos = models.ManyToManyField('self', blank=True)

    # def favoritar_usuario(self, usuario):
    #     self.favoritos.add(usuario)

    # def remover_usuario(self, usuario):
    #     self.favoritos.remove(usuario)


class Funcionario(models.Model):
    NOTAS = [
        (-2, '😡'),
        (-1, '🙁'),
        (0, '😐'),
        (1, '🙂'),
        (2, '😀')
    ]
    atendimento = models.IntegerField(choices=NOTAS)
    pontualidade = models.IntegerField(choices=NOTAS)
    qualidade = models.IntegerField(choices=NOTAS)
    # experiencia = models.IntegerField(0)
    # nivel = models.IntegerField(0)

    def media(self):
        return (self.atendimento + self.pontualidade + self.qualidade) / 3

    def template(self, atributo):
        return atributo(choices=self.NOTAS)
    
    def soma(self):
        return self.atendimento + self.pontualidade + self.qualidade
    
    def ver_nivel(self):
        self.experiencia = self.soma()
        if(self.experiencia < 5):
            self.nivel = 1
        if(self.experiencia < 10):
            self.nivel = 2
        if(self.experiencia < 20):
            self.nivel = 3
        if(self.experiencia < 30):
            self.nivel = 4
        if(self.experiencia < 50):
            self.nivel = 5
        return self.nivel

    def calcular_xp(self):
        resultado_xp = ""
        if(self.ver_nivel() == 1):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia} / 5"
        if(self.ver_nivel() == 2):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia} / 10"
        if(self.ver_nivel() == 3):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia} / 20"
        if(self.ver_nivel() == 4):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia} / 30"
        if(self.ver_nivel() == 5):
            if(self.experiencia > 50):
                self.experiencia = 50
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia} / 50"
        return resultado_xp
