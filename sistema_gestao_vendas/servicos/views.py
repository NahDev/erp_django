from django.shortcuts import render, redirect
from .forms import ServicoForm
from .models import Servico


def agendar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_servicos")
    else:
        form = ServicoForm()

    return render(request, "servicos/agendar_servicos.html", {"form": form})


def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "servicos/lista_servicos.html", {"servicos": servicos})
