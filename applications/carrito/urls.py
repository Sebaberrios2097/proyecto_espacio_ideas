from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/detail/', views.cart_detail, name='cart_detail'),
]