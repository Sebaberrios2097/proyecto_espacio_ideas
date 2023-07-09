from django.urls import path
from .views import CarruselListView, CarruselCreateView, CarruselUpdateView, CarruselDelete, CarruselEstadoView

urlpatterns = [
    path('carrusel/', CarruselListView.as_view(), name='carrusel_list'),
    path('carrusel_create/', CarruselCreateView.as_view(), name='carrusel_create'),
    path('update/<int:pk>/', CarruselUpdateView.as_view(), name='carrusel_update'),
    path('delete/<int:pk>/', CarruselDelete, name='carrusel_delete'),
    path('carrusel/estado/<int:pk>/', CarruselEstadoView.as_view(), name='carrusel_estado'),
]
