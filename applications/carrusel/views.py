from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import Carrusel

class CarruselListView(ListView):
    model = Carrusel
    template_name = 'carrusel/carrusel_list.html'
    context_object_name = 'carruseles'

class CarruselCreateView(CreateView):
    model = Carrusel
    template_name = 'carrusel/crear_carrusel.html'
    fields = ['titulo', 'encabezado', 'subencabezado', 'imagen', 'estado']
    success_url = reverse_lazy('carrusel_list')

class CarruselUpdateView(UpdateView):
    model = Carrusel
    template_name = 'carrusel/carrusel_update.html'
    fields = ['titulo', 'encabezado', 'subencabezado', 'imagen', 'estado']
    success_url = reverse_lazy('carrusel_list')

def CarruselDelete(request, pk):
    carrusel = get_object_or_404(Carrusel, pk=pk)
    carrusel.delete()
    return redirect('carrusel_list')

class CarruselEstadoView(View):
    def post(self, request, pk):
        carrusel = Carrusel.objects.get(pk=pk)
        estado = request.POST.get('estado')
        carrusel.estado = estado
        carrusel.save()
        return redirect('carrusel_list')  # Reemplaza 'carrusel_list' con el nombre de tu vista de listado de carruseles