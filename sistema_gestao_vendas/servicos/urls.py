from django.urls import path
from . import views

urlpatterns = [
    path("agendar_servico/", views.agendar_servico, name="agendar_servico"),
    path("lista_servicos/", views.lista_servicos, name="lista_servicos"),
]
