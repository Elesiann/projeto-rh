from django.db import models


class Registro(models.Model):
    nome = models.CharField(max_length=100)
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

  
    
    