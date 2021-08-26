from django.db import models
from django.contrib.auth.models import User


class Registro(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    numero = models.IntegerField(null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.IntegerField(null=True)
    tel_1 = models.IntegerField(null=True)
    tel_2 = models.IntegerField(blank=True)


class Sobre(Registro):
    sobrecandidato = models.TextField(blank=False)
    
    def __str__(self):
        return self.sobrecandidato
  
    
    