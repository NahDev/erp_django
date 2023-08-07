# pedidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_pedido, name='criar_pedido'),
    path('registrar_pagamento/<int:pedido_id>/', views.registrar_pagamento, name='registrar_pagamento'),

]
