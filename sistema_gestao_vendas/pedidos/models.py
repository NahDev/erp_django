# pedidos/models.py

from django.db import models
from clientes.models import Cliente
from estoque.models import Produto
from django.db.models.signals import post_save
from django.dispatch import receiver


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    produtos = models.ManyToManyField(Produto, through="ItemPedido")
    STATUS_CHOICES = (
        ("aberto", "Aberto"),
        ("entregue", "Entregue"),
        ("cancelado", "Cancelado"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="aberto")
    # rastreamento = models.OneToOneField(
    #     "logistica.Rastreamento",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="pedido_relacionado",  # Adicionando related_name para resolver o conflito
    # )

    def total_pedido(self):
        return sum(item.subtotal() for item in self.itempedido_set.all())

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nome_empresa}"


@receiver(post_save, sender=Pedido)
def set_status_aberto(sender, instance, **kwargs):
    if (
        instance._state.adding
    ):  # Verifica se o objeto está sendo criado (não atualizado)
        instance.status = "aberto"
        instance.save()


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario


class Pagamento(models.Model):
    pedido = models.OneToOneField("Pedido", on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    gateway = models.CharField(max_length=100)
    referencia_gateway = models.CharField(max_length=100, blank=True, null=True)
    data_pagamento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Pagamento para Pedido {self.pedido.id}"
