# logistica/forms.py

from django import forms
from .models import Roteirizacao


class RoteirizacaoForm(forms.ModelForm):
    class Meta:
        model = Roteirizacao
        fields = ["origem", "destino", "distancia_km", "transporte", "pedidos"]
        widgets = {"pedidos": forms.CheckboxSelectMultiple}
