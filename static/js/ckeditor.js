CKEDITOR.replace('id_descripcion');
CKEDITOR.replace('aviso_personalizacion');

// Función para mostrar u ocultar el campo "aviso_personalizacion"
$(document).ready(function() {
    // Función para mostrar u ocultar el campo "aviso_personalizacion"
    function toggleAvisoPersonalizacion() {
        const aviso = $('#aviso');
        const avisoPersonalizacionContainer = $('#aPersonalizacionContainer');

        if (aviso.val() === "true") {
            avisoPersonalizacionContainer.show();
        } else {
            avisoPersonalizacionContainer.hide();
        }
    }

    // Controlador de eventos para el campo "aviso"
    $('#aviso').on('change', toggleAvisoPersonalizacion);

    // Establecer la visibilidad inicial del campo "aviso_personalizacion"
    toggleAvisoPersonalizacion();
});