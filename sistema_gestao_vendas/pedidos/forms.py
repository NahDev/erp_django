# pedidos/forms.py

from django import forms
from .models import Pedido, ItemPedido, Pagamento


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "data_entrega"]


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ["produto", "quantidade", "preco_unitario"]


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ["valor_total", "gateway", "referencia_gateway", "data_pagamento"]
