// función de vista previa para la sección de crear producto
function mostrarVistaPrevia(input) {
  var contenedor = document.getElementById('vista-previa');
  contenedor.innerHTML = '';
  if (input.files && input.files.length > 0) {
    // Agregar una fila adicional para la cabecera
    var cabecera = document.createElement('div');
    cabecera.classList.add('row', 'mb-3', 'align-items-center');
    var colNombreCabecera = document.createElement('div');
    colNombreCabecera.classList.add('col-md-8');
    var colImgCabecera = document.createElement('div');
    colImgCabecera.classList.add('col-md-4');
    cabecera.appendChild(colNombreCabecera);
    cabecera.appendChild(colImgCabecera);
    var nombreCabecera = document.createElement('span');
    nombreCabecera.innerHTML = 'Nombre de archivo';
    nombreCabecera.classList.add('small', 'd-block', 'text-center');
    colNombreCabecera.appendChild(nombreCabecera);
    var vistaPreviaCabecera = document.createElement('span');
    vistaPreviaCabecera.innerHTML = 'Vista previa';
    vistaPreviaCabecera.classList.add('small', 'd-block', 'text-center');
    colImgCabecera.appendChild(vistaPreviaCabecera);
    contenedor.appendChild(cabecera);

    for (var i = 0; i < input.files.length; i++) {
      var archivo = input.files[i];
      if (archivo.type.match(/^image\//)) {
        crearImagenPrevia(archivo, contenedor);
      }
    }
  }
}

function crearImagenPrevia(archivo, contenedor) {
  var row = document.createElement('div');
  row.classList.add('row', 'mb-3', 'align-items-center');
  var colNombre = document.createElement('div');
  colNombre.classList.add('col-md-8');
  var colImg = document.createElement('div');
  colImg.classList.add('col-md-4');
  var reader = new FileReader();
  reader.onload = function (e) {
    var img = document.createElement('img');
    img.src = e.target.result;
    img.classList.add('img-thumbnail', 'img-fluid');
    colImg.appendChild(img);
  }
  reader.readAsDataURL(archivo);
  var nombre = document.createElement('span');
  nombre.innerHTML = archivo.name;
  nombre.classList.add('small', 'd-block', 'text-center');
  colNombre.appendChild(nombre);
  row.appendChild(colNombre);
  row.appendChild(colImg);
  contenedor.appendChild(row);
}
// Script de manejo de cantidad de productos index
// Manejador de evento de clic para el botón de menos
document.getElementById("btn-minus").addEventListener("click", function () {
  let cantidad = parseInt(document.getElementById("btn-cantidad").textContent);
  if (cantidad > 1) {
    document.getElementById("btn-cantidad").textContent = cantidad - 1;
  }
});

// Manejador de evento de clic para el botón de más
document.getElementById("btn-plus").addEventListener("click", function () {
  let cantidad = parseInt(document.getElementById("btn-cantidad").textContent);
  if (cantidad < 10) {
    document.getElementById("btn-cantidad").textContent = cantidad + 1;
  }
});

// Script de manejo de cantidad de productos detalle
$(document).ready(function () {
  // Agregar evento de clic al botón de decremento
  $('#btn-minus').click(function () {
    // Obtener el valor actual de la cantidad
    var cantidad = parseInt($('#btn-cantidad').val());
    // Si el valor actual es mayor que el valor mínimo, disminuir en 1
    if (cantidad > parseInt($('#btn-cantidad').attr('min'))) {
      $('#btn-cantidad').val(cantidad - 1);
    }
  });

  // Agregar evento de clic al botón de incremento
  $('#btn-plus').click(function () {
    // Obtener el valor actual de la cantidad
    var cantidad = parseInt($('#btn-cantidad').val());
    // Obtener el valor del stock
    var stock = parseInt($('input[data-stock]').data('stock'));
    // Obtener el valor máximo
    var max = parseInt($('#btn-cantidad').attr('max'));

    // Si el valor actual es menor que el valor máximo y menor que el stock, aumentar en 1
    if (cantidad < max && cantidad < stock) {
      $('#btn-cantidad').val(cantidad + 1);
    }
  });
});


// Script de manejo de funcionalidad de las imagenes al pie del carrusel de det_producto
$(document).ready(function () {
  $('.thumbnail-img').on('click', function () {
    var selectedImageSrc = $(this).data('src');
    $('#carouselExampleFade .carousel-item').each(function () {
      var carouselImage = $(this).find('img');
      if (carouselImage.attr('src') === selectedImageSrc) {
        $(this).addClass('active');
      } else {
        $(this).removeClass('active');
      }
    });
  });
});