from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(null=True, unique=True)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    favoritos = models.ManyToManyField('self', blank=True)
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-id"]
    
    def __str__(self):
        return self.email


    # def favoritar_usuario(self, usuario):
    #     self.favoritos.add(usuario)

    # def remover_usuario(self, usuario):
    #     self.favoritos.remove(usuario)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="usuário")
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["-id"]

    def __str__(self):
        return self.email

    @property
    def email(self):
        return self.usuario.email


class Atendimento(models.Model):
    NOTAS = [
        (-2, '😡'),
        (-1, '🙁'),
        (0, '😐'),
        (1, '🙂'),
        (2, '😀')
    ]
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="atendimentos", verbose_name="Funcionário", null=True)
    atendimento = models.IntegerField(choices=NOTAS)
    pontualidade = models.IntegerField(choices=NOTAS)
    qualidade = models.IntegerField(choices=NOTAS)
    # experiencia = models.IntegerField(0)
    # nivel = models.IntegerField(0)

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.funcionario.email} {self.id}"
    
    def media(self):
        return (self.atendimento + self.pontualidade + self.qualidade) / 3

    def template(self, atributo):
        return atributo(choices=self.NOTAS)
    
    def soma(self):
        return self.atendimento + self.pontualidade + self.qualidade
    
    def experiencia(self):
        return min([self.soma(), 50])
    
    def ver_nivel(self):        

        if(self.experiencia() < 5):
            nivel = 1
        elif(self.experiencia() < 10):
            nivel = 2
        elif(self.experiencia() < 20):
            nivel = 3
        elif(self.experiencia() < 30):
            nivel = 4
        elif(self.experiencia() <= 50):
            nivel = 5
        return nivel

    def calcular_xp(self):
        resultado_xp = ""
        if(self.ver_nivel() == 1):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia()} / 5"
        elif(self.ver_nivel() == 2):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia()} / 10"
        elif(self.ver_nivel() == 3):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia()} / 20"
        elif(self.ver_nivel() == 4):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia()} / 30"
        elif(self.ver_nivel() == 5):
            resultado_xp = f"Nível: {self.ver_nivel()}\nExperiência: {self.experiencia()} / 50"
        return resultado_xp



