from applications.personalizacion.models import Personalizacion

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self, producto, quantity=1):
        personalizacion_id = self.request.session.get('personalizacion_id')  # Obtén el ID de la personalización de la sesión (si existe)

        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": quantity,
                "img_principal": producto.img_principal.url,
            }

            if personalizacion_id:
                personalizacion = Personalizacion.objects.get(id=personalizacion_id)
                self.cart[producto.id]["personalizacion_id"] = personalizacion.id
                self.cart[producto.id]["nombre_personalizacion"] = personalizacion.nombre
                del self.request.session['personalizacion_id']  # Elimina el ID de la personalización de la sesión

        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] += quantity
                    break

        self.save()


    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def decrement(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True