from django.shortcuts import render, redirect
from .forms import ClienteForm


def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_clientes")
    else:
        form = ClienteForm()
    return render(request, "clientes/cadastrar_cliente.html", {"form": form})
