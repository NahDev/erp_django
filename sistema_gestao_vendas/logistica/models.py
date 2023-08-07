from django.db import models


class Transporte(models.Model):
    nome = models.CharField(max_length=100)
    capacidade_carga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Roteirizacao(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    pedidos = models.ManyToManyField("pedidos.Pedido", related_name="roteirizacoes")

    def __str__(self):
        return f"Roteirização de {self.origem} para {self.destino}"


class Rastreamento(models.Model):
    pedido_relacionado = models.OneToOneField(
        "pedidos.Pedido", on_delete=models.CASCADE, related_name="rastreamento_pedido"
    )  # Utilizando um nome diferente para o campo
    data_entrega = models.DateTimeField()
    local_entrega = models.CharField(max_length=100)

    def __str__(self):
        return f"Rastreamento do Pedido {self.pedido_relacionado.id}"
