from django.urls import path
from .views import UsuarioCreateView, login_view, logout_view


urlpatterns = [
    path('registrar_usuario/', UsuarioCreateView.as_view(), name='registrar_usuario'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]