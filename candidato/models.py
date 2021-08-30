from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    relacao_user = models.ForeignKey(User, on_delete=models.CASCADE),
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    estado_civil = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    numero = models.IntegerField(null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.IntegerField(null=True)
    tel_1 = models.CharField(max_length=50)
    tel_2 = models.CharField(max_length=50)


class Sobre(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    sobrecandidato = models.TextField(verbose_name='sobreCandidato')
    

'''class Experiencias(models.Model):
    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    inicio = models.DateField(null=True)
    fim = models.DateField(null=True)
    local = models.CharField(max_length=50)
    atividades = models.TextField(null=True, verbose_name='atividadesOuConquistas')
    comprovante = models.FileField(null=True)


class Cursos(models.Model):
    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=50)
    data = models.DateField(null=True)
    local_curso = models.CharField(max_length=50)
    duracao_horas = models.IntegerField()
    certificado = models.FileField(null=True)
 '''