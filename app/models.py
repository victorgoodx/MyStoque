from django.db import models

# Create your models here.
class Produtos(models.Model):
    produto = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=30)
    ano_validade = models.IntegerField()