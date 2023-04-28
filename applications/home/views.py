from django.shortcuts import render
from django.views.generic import TemplateView
from applications.producto.models import Producto

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_recientes'] = Producto.objects.all().order_by('-id')[:4]  # Cambia al número de productos que desees mostrar
        return context