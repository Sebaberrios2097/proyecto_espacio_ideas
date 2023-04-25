from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin #libreria para restringir el acceso a usuarios no logueados
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import CustomUserCreationForm   
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        # procesa los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        # llama a la función authenticate para autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirige al usuario a la página de inicio
            print('Usuario autenticado')
            return redirect('home')
        else:
            print('Usuario no autenticado')
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    # muestra el formulario de inicio de sesión
    return render(request, 'usuario/login.html')


class UserListView(ListView):
    model = User

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    context_object_name = 'usuario'
    template_name = 'usuario/registrar_usuario.html'

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
