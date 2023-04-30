from django.urls import path
from . import views

urlpatterns = [
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
]
