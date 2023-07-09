// enviar la cantidad seleccionada al carrito de compras
$(document).ready(function() {
    const addToCartButton = $('#add-to-cart');
    const quantityInput = $('#btn-cantidad');

    addToCartButton.on('click', function(event) {
      event.preventDefault();
      const url = addToCartButton.attr('data-href');
      const quantity = quantityInput.val();
      addToCartButton.attr('data-cantidad', quantity);
      window.location.href = `${url}?cantidad=${quantity}`;
    });
  });

