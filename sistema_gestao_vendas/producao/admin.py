from django.contrib import admin
from .models import MateriasPrimas, Producao, UsoMateriaPrima


admin.site.register(MateriasPrimas)
admin.site.register(Producao)
admin.site.register(UsoMateriaPrima)
