from django.db import models


class Registro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)
    tel_1 = models.CharField(max_length=50)
    tel_2 = models.CharField(max_length=50, blank=True)
    
    