from django.shortcuts import render

# Create your views here.

def panel_gestion(request):
    return render(request, 'gestion/panel_gestion.html')