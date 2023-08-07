# logistica/views.py

from django.shortcuts import render, redirect
from .models import Transporte, Roteirizacao, Rastreamento
from pedidos.models import Pedido


def criar_roteirizacao(request):
    if request.method == "POST":
        origem = request.POST["origem"]
        destino = request.POST["destino"]
        distancia_km = request.POST["distancia_km"]
        transporte_id = request.POST["transporte"]

        transporte = Transporte.objects.get(pk=transporte_id)
        roteirizacao = Roteirizacao.objects.create(
            origem=origem,
            destino=destino,
            distancia_km=distancia_km,
            transporte=transporte,
        )

        pedidos_selecionados = request.POST.getlist("pedidos")
        for pedido_id in pedidos_selecionados:
            pedido = Pedido.objects.get(pk=pedido_id)
            roteirizacao.pedidos.add(pedido)

        roteirizacao.save()

        return redirect("lista_roteirizacao")

    transportes = Transporte.objects.all()
    pedidos = Pedido.objects.filter(roteirizacao__isnull=True)

    return render(
        request,
        "logistica/criar_roteirizacao.html",
        {"transportes": transportes, "pedidos": pedidos},
    )


def lista_roteirizacao(request):
    roteirizacoes = Roteirizacao.objects.all()
    return render(
        request, "logistica/lista_roteirizacao.html", {"roteirizacoes": roteirizacoes}
    )
