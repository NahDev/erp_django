
from django.db import models
from estoque.models import Produto


class MateriasPrimas(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Producao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    quantidade_produzida = models.PositiveIntegerField()
    materias_primas = models.ManyToManyField(MateriasPrimas, through="UsoMateriaPrima")

    def __str__(self):
        return f"Produção de {self.produto.nome_empresa} - {self.data_inicio}"


class UsoMateriaPrima(models.Model):
    producao = models.ForeignKey(Producao, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriasPrimas, on_delete=models.CASCADE)
    quantidade_utilizada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producao} - {self.materia_prima}"
