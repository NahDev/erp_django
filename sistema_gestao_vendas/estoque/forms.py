from django import forms
from .models import Produto, Categoria


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome_empresa",
            "marca",
            "quantidade",
            "preco",
            "dimensao",
            "data_entrada",
            "previsao_saida",
            "categoria",
        ]

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields["categoria"].queryset = Categoria.objects.all()
