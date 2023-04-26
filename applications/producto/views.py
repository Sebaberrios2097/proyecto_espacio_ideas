<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto, Categoria
from .forms import CustomProductoCreationForm, CustomCategoriaCreationForm
from django.urls import reverse_lazy

#Crate de Producto
class ProductoCreateView(CreateView):
    model = Producto
    form_class = CustomProductoCreationForm
    success_url = reverse_lazy('productos')
    context_object_name = 'producto'
    template_name = 'producto/crear_producto.html'

#Listar productos
class ProductoListView(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'producto/productos.html'


#Actualizar producto
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = CustomProductoCreationForm
    success_url = reverse_lazy('productos')
    context_object_name = 'producto'
    template_name = 'producto/editar_producto.html'

#Eliminar productos
def borrar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    producto.delete()
    return redirect('productos') #Implementar modal para consultar si se esta seguro de la eliminación del registro

#Crear categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CustomCategoriaCreationForm
    success_url = reverse_lazy('categorias')
    context_object_name = 'categoria'
    template_name = 'producto/crear_categoria.html'

#Listar categorías
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'producto/categorias.html'

#Actualizar categoría
class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CustomCategoriaCreationForm
    success_url = reverse_lazy('categorias')
    context_object_name = 'categoria'
    template_name = 'producto/editar_categoria.html'

#Eliminar categoría
def borrar_categoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return redirect('categorias')
>>>>>>> Seba
