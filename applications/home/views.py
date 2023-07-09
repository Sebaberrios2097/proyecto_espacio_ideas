from django.views.generic import TemplateView
from applications.producto.models import Producto
from applications.carrusel.models import Carrusel
from django.views.generic import View
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_recientes'] = Producto.objects.all().order_by('-id')[:5]
        context['carruseles'] = Carrusel.objects.filter(estado=True)
        context['productos_mas_vendidos'] = Producto.objects.order_by('-cantidad_vendidos')[:5]
        return context