from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *
from applications.producto.models import Producto
from .forms import PersonalizacionCreateForm
from django.contrib import messages

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

        # Guarda el ID de la personalización en la sesión
        self.request.session['personalizacion_id'] = self.object.id
        messages.success(self.request, 'Personalización creada exitosamente.')  # Añade un mensaje de éxito
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto_id = self.kwargs['producto_id']
        context['producto'] = get_object_or_404(Producto, id=producto_id)
        return context
    
    def get_success_url(self):
        producto_id = self.kwargs['producto_id']
        return reverse_lazy('product_detail', kwargs={'pk': producto_id})

def personalizacion_detail(request, pk):
    personalizacion = get_object_or_404(Personalizacion, id=pk)
    imagenes = ImagenPersonalizacion.objects.filter(personalizacion=personalizacion)
    return render(request, 'personalizacion/personalizacionDetail.html', {'personalizacion': personalizacion, 'imagenes': imagenes})

def personalizacion_delete(request, pk):
    personalizacion = get_object_or_404(Personalizacion, id=pk)
    producto_id = personalizacion.producto.id
    personalizacion.delete()
    messages.success(request, 'Personalización eliminada exitosamente.')  # Añade un mensaje de éxito
    return reverse_lazy('product_detail', kwargs={'pk': producto_id})

def personalizacion_edit(request, pk):
    personalizacion = get_object_or_404(Personalizacion, id=pk)
    imagenes = ImagenPersonalizacion.objects.filter(personalizacion=personalizacion)
    return render(request, 'personalizacion/personalizacionEdit.html', {'personalizacion': personalizacion, 'imagenes': imagenes})

def personalizacion_update(request, pk):
    personalizacion = get_object_or_404(Personalizacion, id=pk)
    imagenes = ImagenPersonalizacion.objects.filter(personalizacion=personalizacion)
    imagenes.delete()
    imagenes = request.FILES.getlist('imagenes[]')
    for imagen in imagenes:
        ImagenPersonalizacion.objects.create(imagen=imagen, personalizacion=personalizacion)
    messages.success(request, 'Personalización actualizada exitosamente.')  # Añade un mensaje de éxito
    return reverse_lazy('personalizacion_detail', kwargs={'pk': pk})

class personalizacion_list(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'personalizacion/lista_perso.html'