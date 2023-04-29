from django.urls import path
from .views import PersonalizacionCreate

urlpatterns = [
    path('personalizarProducto/<producto_id>/', PersonalizacionCreate.as_view(), name='producto_personalizar'),
]
