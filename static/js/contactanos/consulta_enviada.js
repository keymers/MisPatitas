function messageConsultaEnviada() {

    var nombre = $("#id_txtNombre").val();
    var correo = $("#id_txtCorreo").val();
    var escriba = $("#id_txtEscriba").val();

    var larNombre = nombre.length;
    var larCorreo = correo.length;
    var larEscriba = escriba.length;

    if ( (larNombre >= 5) && (larCorreo >= 5) && (larEscriba >= 30)
    ) {
        window.alert("Consulta enviada satisfactoriamente!!! ")
    }
 
}