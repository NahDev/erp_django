from django.db import models
from clientes.models import Cliente


class Recurso(models.Model):
    nome = models.CharField(max_length=100)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrato com {self.cliente.nome_empresa}"


class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField()
    realizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Serviço para {self.cliente.nome_empresa} - {self.recurso.nome}"
