from django.urls import path
from applications.carrusel.views import CarruselListView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('carrusel/', CarruselListView.as_view(), name='carrusel_list'),
]
