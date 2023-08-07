
from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_producao, name='registrar_producao'),
    path('lista/', views.lista_producao, name='lista_producao'),
]
