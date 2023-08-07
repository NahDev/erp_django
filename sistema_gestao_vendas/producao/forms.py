# producao/forms.py

from django import forms
from .models import Producao, UsoMateriaPrima

class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = ['produto', 'data_inicio', 'quantidade_produzida']

class UsoMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = UsoMateriaPrima
        fields = ['materia_prima', 'quantidade_utilizada']
