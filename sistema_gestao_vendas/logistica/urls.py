
from django.urls import path
from . import views

urlpatterns = [
    path("criar_roteirizacao/", views.criar_roteirizacao, name="criar_roteirizacao"),
    path("lista_roteirizacao/", views.lista_roteirizacao, name="lista_roteirizacao"),
]
