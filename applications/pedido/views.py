from django.shortcuts import render, redirect
from .models import Pedido, DetallePedido, Producto
from applications.carrito.cart import Cart
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from django.views.generic import DetailView
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.db.models import F


commerce_code_integracion = '597055555532'
api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
mode = 'INTEGRATION'
"""
Tarjetas de prueba:
VISA: 4051 8856 0044 6623 Genera transacciones aprobadas
MASTER: 5186 0595 5959 0568 Genera transacciones rechazadas
Rut: 11.111.111-1
Clave: 123
"""

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

        # Aquí inicia la creación de la transacción de Webpay:
        buy_order = str(pedido.transaction_id)
        session_id = str(request.user)
        amount = str(cart.get_total())
        return_url = request.build_absolute_uri(reverse('webpay_response'))

        response = Transaction(WebpayOptions(commerce_code_integracion, api_key, mode)).create(buy_order, session_id, amount, return_url)

        url = response['url']
        token = response['token']

        # Guarda el token de Webpay en el Pedido:
        pedido.webpay_token = token
        pedido.save()

        print(response)

        return redirect(f'{url}?TBK_TOKEN={token}')
    
def webpay_response(request):
    if request.method == 'GET' and 'token_ws' in request.GET:
        token = request.GET.get('token_ws')
        response = Transaction(WebpayOptions(commerce_code_integracion, api_key, mode)).commit(token)
        cart = Cart(request)

        if response['status'] == 'AUTHORIZED':
            pedido = Pedido.objects.get(webpay_token=token)
            pedido.estado = 'PAGADO'
            pedido.save()
            
            # Actualizar el stock de los productos comprados y sumar la cantidad vendida
            for item in cart.cart.values():
                producto = Producto.objects.get(id=item['producto_id'])
                cantidad_comprada = item['cantidad']
                producto.stock -= cantidad_comprada
                producto.save()

                Producto.objects.filter(id=item['producto_id']).update(cantidad_vendidos=F('cantidad_vendidos') + cantidad_comprada)

            cart.clear()
            return render(request, 'pedido/pago_exitoso.html', {'response': response, 'pedido': pedido})
        else:
            pedido = Pedido.objects.get(webpay_token=token)
            pedido.delete()
            if response['status'] == 'ABORTED':
                return redirect('pago_fallido', error='La transacción ha sido abortada.')
            elif response['status'] == 'FAILED':
                return redirect('pago_fallido', error='La transacción ha sido rechazada.')

    elif request.method == 'POST':
        return redirect('pago')

    return redirect('cart_detail')

def pago_fallido(request, error):
    return render(request, 'pedido/pago_fallido.html', {'error': error})

def lista_pedidos(request):
    pedidos = Pedido.objects.all().prefetch_related('detallepedido_set', 'detallepedido_set__producto', 'detallepedido_set__personalizacion')
    return render(request, 'pedido/lista_pedidos.html', {'pedidos': pedidos})

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido/detalle_pedido.html'
    context_object_name = 'pedido'