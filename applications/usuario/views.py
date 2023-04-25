from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import UserExtra
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class UsuarioCreateView(CreateView):
    model = UserExtra
    template_name = "usuario/registrar_usuario.html"
    context_object_name = "usuario"
    form_class = UserForm
    success_url = reverse_lazy('home')

def login_view(request):
    if request.method == 'POST':
        #Procesa los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Llama a la función 'authenticate' de Django para verificar las credenciales
        user = authenticate(username=username, password=password)

        if user is not None:
            #Si el usuario es válido, inicia sesion y redirige a la pagina de inicio
            login(request, user)
            return redirect('home')
        else:
            #Si no es válido, muestra un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos')
            
    return render(request, 'usuario/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
