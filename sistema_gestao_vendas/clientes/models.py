# clientes/models.py

from django.db import models


class Cliente(models.Model):
    nome_empresa = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    cnpj_cpf = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome_empresa
