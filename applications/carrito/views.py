from django.shortcuts import render, get_object_or_404, redirect
from applications.producto.models import Producto
from .cart import Cart
from applications.personalizacion.models import Personalizacion


def cart_add(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    personalizacion_id = request.GET.get('personalizacion_id')
    if personalizacion_id:
        product.personalizacion = get_object_or_404(Personalizacion, id=personalizacion_id)
    cart = Cart(request)
    quantity = int(request.GET.get('cantidad', 1))
    cart.add(product, quantity=quantity)
    return redirect("cart_detail")


def cart_remove(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect("cart_detail")

def cart_decrement(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    cart = Cart(request)
    cart.decrement(product)
    return redirect("cart_detail")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

def cart_detail(request):
    cart = Cart(request)
    total = 0
    for key, value in cart.cart.items():
        subtotal = int(value['precio']) * value['cantidad']
        value['subtotal'] = subtotal
        value['precio'] = int(value['precio'])  # Agregar el subtotal al diccionario del producto
        total += subtotal

    context = {'cart': cart, 'total': int(total)}
    return render(request, 'carrito/cart_detail.html', context)

