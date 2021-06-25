$(document).ready(function() {
    $("#contacto").validate({
        rules: {
            "txtNombre": {
                required: true,
                minlength: 5
            },
            "txtCorreo": {
                required: true,
                email: true
            },
            "txtEscriba": {
                required: true,
                minlength: 30
            }
        },
        messages: {
            "txtNombre": {
                required: 'Ingrese su nombre',
                minlength: 'Minimo 5 caracteres'
            },
            "txtCorreo": {
                required: 'Ingrese su correo',
                email: 'No cumple formato correo@ejemplo.com'
            },
            "txtEscriba": {
                required: 'Ingrese su consulta',
                minlength: 'Minimo 30 caracteres'
            }
        }

    });
});