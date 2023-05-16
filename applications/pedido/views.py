from django.shortcuts import render, redirect
from .models import Pedido, DetallePedido
from applications.carrito.cart import Cart
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions

from django.urls import reverse
from django.http import Http404


commerce_code_integracion = '597055555532'
api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
mode = 'INTEGRATION'

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
    
# def pago_exitoso(request, pedido_id):
#     try:
#         pedido = Pedido.objects.get(id=pedido_id)
#         transaction_id = pedido.transaction_id
#     except Pedido.DoesNotExist:
#         raise Http404("Pedido no existe")
#     return render(request, 'pedido/pago_exitoso.html', {'pedido': pedido, 'transaction_id': transaction_id})

# def pago_fallido(request):
#     return render(request, 'pedido/pago_fallido.html')

def webpay_response(request):
    if request.method == 'GET' and 'token_ws' in request.GET:
        token = request.GET.get('token_ws')
        response = Transaction(WebpayOptions(commerce_code_integracion, api_key, mode)).commit(token)
        cart = Cart(request)

        if response['status'] == 'AUTHORIZED':
            pedido = Pedido.objects.get(webpay_token=token,)
            transaction_id = pedido.transaction_id
            pedido.estado = 'PAGADO'
            pedido.save()
            cart.clear()
            print(response)
            return render(request, 'pedido/pago_exitoso.html', {'response': response, 'pedido': pedido})
        else:
            pedido = Pedido.objects.get(webpay_token=token)
            pedido.delete()
            print(response)
            return render(request, 'pedido/pago_fallido.html', {'response': response})

    elif request.method == 'POST':
        return redirect('pago')