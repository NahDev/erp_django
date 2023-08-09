from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_empresa = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateField()
    previsao_saida = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_empresa + " - " + self.marca
