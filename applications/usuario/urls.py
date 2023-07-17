from django.urls import path
from .views import *


urlpatterns = [
    path('registrar_usuario/', UsuarioCreateView.as_view(), name='registrar_usuario'),
    path('editar_usuario/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/<id>', perfil_view, name='view_profile'),
]