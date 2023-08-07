from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "nome_empresa",
            "responsavel",
            "endereco",
            "telefone",
            "email",
            "cnpj_cpf",
        ]
