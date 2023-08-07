
from django.shortcuts import render, redirect
from .forms import ProducaoForm, UsoMateriaPrimaForm
from .models import Producao

def registrar_producao(request):
    if request.method == "POST":
        producao_form = ProducaoForm(request.POST)
        uso_materia_prima_form = UsoMateriaPrimaForm(request.POST)

        if producao_form.is_valid() and uso_materia_prima_form.is_valid():
            producao = producao_form.save()
            uso_materia_prima = uso_materia_prima_form.save(commit=False)
            uso_materia_prima.producao = producao
            uso_materia_prima.save()
            return redirect("lista_producao")
    else:
        producao_form = ProducaoForm()
        uso_materia_prima_form = UsoMateriaPrimaForm()

    return render(
        request,
        "producao/registrar_producao.html",
        {
            "producao_form": producao_form,
            "uso_materia_prima_form": uso_materia_prima_form,
        },
    )


def lista_producao(request):
    producoes = Producao.objects.all()
    return render(request, "producao/lista_producao.html", {"producoes": producoes})
