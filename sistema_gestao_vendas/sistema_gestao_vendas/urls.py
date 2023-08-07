# sistema_gestao_vendas/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("clientes.urls")),
    path("estoque/", include("estoque.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("vendas/", include("vendas.urls")),
    path("producao/", include("producao.urls")),
    path("logistica/", include("logistica.urls")),
    path("servicos/", include("servicos.urls")),
]
