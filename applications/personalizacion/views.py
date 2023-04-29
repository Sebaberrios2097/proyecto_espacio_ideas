from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from applications.producto.models import Producto
from .forms import PersonalizacionCreateForm

class PersonalizacionCreate(CreateView):
    model = Personalizacion
    form_class = PersonalizacionCreateForm
    template_name = 'personalizacion/personalizarProducto.html'
    context_object_name = 'personalizacion'

    def get_initial(self):
        initial = super().get_initial()
        producto_id = self.kwargs['producto_id']
        initial['producto'] = get_object_or_404(Producto, id=producto_id)
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        imagenes = self.request.FILES.getlist('imagenes[]')
        for imagen in imagenes:
            ImagenPersonalizacion.objects.create(imagen=imagen, personalizacion=self.object)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto_id = self.kwargs['producto_id']
        context['producto'] = get_object_or_404(Producto, id=producto_id)
        return context
    
    def get_success_url(self):
        producto_id = self.kwargs['producto_id']
        return reverse_lazy('product_detail', kwargs={'pk': producto_id})
