from django.urls import path
from .views import *

urlpatterns = [
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    # path('pago_exitoso/<int:pedido_id>/', pago_exitoso, name='pago_exitoso'),
    # path('pago_fallido/', pago_fallido, name='pago_fallido'),
    path('pago_fallido/<str:error>/', pago_fallido, name='pago_fallido'),
    path('webpay_response/', webpay_response, name='webpay_response'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido_detail'),
]
