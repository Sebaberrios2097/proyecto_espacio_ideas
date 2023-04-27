from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar_producto/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/', ProductoListView.as_view(), name='productos'),
    path('actualizar_producto/<pk>', ProductoUpdateView.as_view(), name='producto_update'),
    path('borrar_producto/<pk>', borrar_producto, name='producto_delete'),
    path('crear_categoria/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('actualizar_categoria/<pk>', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('borrar_categoria/<pk>', borrar_categoria, name='categoria_delete'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)