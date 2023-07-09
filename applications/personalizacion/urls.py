from django.urls import path
from .views import PersonalizacionCreate, personalizacion_list

urlpatterns = [
    path('personalizarProducto/<producto_id>/', PersonalizacionCreate.as_view(), name='producto_personalizar'),
    path('personalizaciones/', personalizacion_list.as_view(), name='perso_views'),
]
