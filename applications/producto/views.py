<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Producto, Categoria, ImagenProducto
from .forms import CustomProductoCreationForm, CustomCategoriaCreationForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View

def es_superusuario(user):
    return user.is_superuser

class SuperuserRequiredMixin(UserPassesTestMixin):
    login_url = '/login/'

    def test_func(self):
        return es_superusuario(self.request.user)
    
#Crate de Producto
class ProductoCreateView(SuperuserRequiredMixin, CreateView):
    model = Producto
    form_class = CustomProductoCreationForm
    success_url = reverse_lazy('productos')
    context_object_name = 'producto'
    template_name = 'producto/crear_producto.html'

    def form_valid(self, form):
        # Obtenemos las imágenes del campo de entrada de archivo múltiple
        imagenes = self.request.FILES.getlist('imagenes[]')

        # Llamamos al método form_valid del padre para guardar la información del producto en la base de datos
        response = super().form_valid(form)

        # Guardamos cada imagen en el sistema de archivos y las relacionamos con el producto recién creado
        for imagen in imagenes:
            ImagenProducto.objects.create(imagen=imagen, producto=self.object)

        # Devolvemos la respuesta
        return response

#Listar productos
class ProductoListView(SuperuserRequiredMixin, ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'producto/productos.html'


#Actualizar producto
class ProductoUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Producto
    form_class = CustomProductoCreationForm
    success_url = reverse_lazy('productos')
    context_object_name = 'producto'
    template_name = 'producto/editar_producto.html'
    
#Eliminar productos
@user_passes_test(es_superusuario)
def borrar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    producto.delete()
    return redirect('productos') #Implementar modal para consultar si se esta seguro de la eliminación del registro

#Crear categoría
class CategoriaCreateView(SuperuserRequiredMixin, CreateView):
    model = Categoria
    form_class = CustomCategoriaCreationForm
    context_object_name = 'categoria'
    template_name = 'producto/crear_categoria.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url == 'producto_create':
            self.request.session['next_url'] = next_url
            return reverse('producto_create')
        else:
            return reverse_lazy('categorias')

#Listar categorías
class CategoriaListView(SuperuserRequiredMixin, ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'producto/categorias.html'

#Actualizar categoría
class CategoriaUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Categoria
    form_class = CustomCategoriaCreationForm
    success_url = reverse_lazy('categorias')
    context_object_name = 'categoria'
    template_name = 'producto/editar_categoria.html'

@user_passes_test(es_superusuario)
#Eliminar categoría
def borrar_categoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return redirect('categorias')
<<<<<<< HEAD
>>>>>>> Seba
=======

class ProductoDetailView(DetailView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'producto/det_producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagenes'] = ImagenProducto.objects.filter(producto=self.object)
        return context

class ver_prod_usuarios(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'producto/list_productos.html'

def productos_especiales(request):
    productos = Producto.objects.filter(categoria__nombre='Especiales')
    context = {'productos': productos}
    return render(request, 'producto/prod_especiales.html', context)
>>>>>>> Seba
