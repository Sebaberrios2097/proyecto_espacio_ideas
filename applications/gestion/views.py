from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def es_superusuario(user):
    return user.is_superuser

@user_passes_test(es_superusuario, login_url='/login/')
def panel_gestion(request):
    return render(request, 'gestion/panel_gestion.html')