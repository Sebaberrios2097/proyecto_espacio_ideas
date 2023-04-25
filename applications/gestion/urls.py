from django.urls import path
from .views import panel_gestion

urlpatterns = [
    path('panel_gestion/', panel_gestion, name='panel_gestion'),
]