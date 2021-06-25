
// notacion abreviada
$(function () {
    $("#submit-form").click(function (event) {
        event.preventDefault();

        var nombre = $("#nombre").val();
        var peso = $("#peso").val();
        var estatura = $("#estatura").val();
        var edad = $("#edad").val();
        var especie = $("#especie").val();

        var fila = '<tr><th>' + nombre + '</th><th>' + peso + '</th><th>' + estatura + '</th><th>' + edad + '</th><th>' + especie + '</th></tr>';

        $('#tablaprueba>tbody').append(fila);

        var documento = $("#tablaprueba");
        documento.css("background-color", "#7584");

    });
    //   cierre del click de submint
});
//   cierre del ready

