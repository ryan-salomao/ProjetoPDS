from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=50)
    senha = models.CharField(max_length=6)

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

    def media(self):
        return (self.atendimento + self.pontualidade + self.qualidade) / 3

    def template(self, atributo):
        return atributo(choices=self.NOTAS)
    
    def soma(self):
        return self.atendimento + self.pontualidade + self.qualidade
    #usar p/ funcionalidade xp