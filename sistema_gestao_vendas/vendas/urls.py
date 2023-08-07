# vendas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("acompanhar/", views.acompanhar_vendas, name="acompanhar_vendas"),
]

urlpatterns = [
    path(
        "acompanhar/",
        views.acompanhar_vendas,
        name="acompanhar_vendas"),
    path(
        "relatorio/periodo/",
        views.relatorio_vendas_periodo,
        name="relatorio_vendas_periodo",
    ),
    path(
        "relatorio/produto/",
        views.relatorio_vendas_produto,
        name="relatorio_vendas_produto",
    ),
    path(
        "relatorio/cliente/",
        views.relatorio_vendas_cliente,
        name="relatorio_vendas_cliente",
    ),
]
