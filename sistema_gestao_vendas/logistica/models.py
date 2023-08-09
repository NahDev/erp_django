from django.db import models


class Veiculo(models.Model):
    empresa = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    capacidade_carga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.empresa


class Trajeto(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_entrega = models.DateTimeField()
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2)
    transpotadora = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pedidos = models.ManyToManyField("pedidos.Pedido", related_name="Trajeto")

    def __str__(self):
        return f"Roteirização de {self.origem} para {self.destino}"


# class Rastreamento(models.Model):
#     pedido_relacionado = models.OneToOneField(
#         "pedidos.Pedido", on_delete=models.CASCADE, related_name="rastreamento_pedido"
#     )  # Utilizando um nome diferente para o campo
#     data_entrega = models.DateTimeField()
#     local_entrega = models.CharField(max_length=100)

#     def __str__(self):
#         return f"Rastreamento do Pedido {self.pedido_relacionado.id}"
