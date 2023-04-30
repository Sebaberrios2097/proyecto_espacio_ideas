from django.shortcuts import render, redirect
from .models import Pedido, DetallePedido
from applications.carrito.cart import Cart

def crear_pedido(request):
    if request.method == 'POST':
        cart = Cart(request)
        pedido = Pedido(usuario=request.user)
        pedido.save()

        for item in cart.cart.values():
            detalle_pedido = DetallePedido(
                pedido=pedido,
                producto_id=item['producto_id'],
                personalizacion_id=item.get('personalizacion_id'),
                cantidad=item['cantidad'],
                precio=item['precio']
            )
            detalle_pedido.save()

        cart.clear()
        return redirect('home')

    return render(request, 'crear_pedido.html')  # Cambia 'crear_pedido.html' por la plantilla HTML que estés utilizando
