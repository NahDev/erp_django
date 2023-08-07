from django.shortcuts import render, redirect
from .forms import PedidoForm, ItemPedidoForm, PagamentoForm
from .models import Pedido, Pagamento


def criar_pedido(request):
    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
        item_form = ItemPedidoForm(request.POST)

        if pedido_form.is_valid() and item_form.is_valid():
            pedido = pedido_form.save()
            item = item_form.save(commit=False)
            item.pedido = pedido
            item.save()
            return redirect("lista_pedidos")
    else:
        pedido_form = PedidoForm()
        item_form = ItemPedidoForm()

    return render(
        request,
        "pedidos/criar_pedido.html",
        {"pedido_form": pedido_form, "item_form": item_form},
    )


def registrar_pagamento(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    if request.method == "POST":
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.pedido = pedido
            pagamento.save()
            return redirect(
                "acompanhar_vendas"
            )  # Substitua 'acompanhar_vendas' pela URL correta para acompanhar as vendas.
    else:
        form = PagamentoForm()

    return render(
        request, "pedidos/registrar_pagamento.html", {"form": form, "pedido": pedido}
    )
