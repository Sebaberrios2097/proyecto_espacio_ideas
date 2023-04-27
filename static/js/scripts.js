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
    reader.onload = function(e) {
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
