/*FORMULARIO DE PAGO - TIENDA COAST*/

document.addEventListener("DOMContentLoaded", function() {

    // Guardamos en variables todos los elementos importantes del formulario
    var formularioPago = document.getElementById("formularioPago");
    var mensajeExito = document.getElementById("mensajeExito");

    var campoNombre = document.getElementById("nombreUsuario");
    var campoApellido = document.getElementById("apellidoUsuario");
    var campoDni = document.getElementById("dniUsuario");
    var campoDireccion = document.getElementById("direccionUsuario");
    var campoNumeroTarjeta = document.getElementById("numeroTarjeta");
    var campoNombreTarjeta = document.getElementById("nombreTarjeta");
    var campoVencimiento = document.getElementById("vencimientoTarjeta");
    var campoCvv = document.getElementById("cvvTarjeta");

    // Cuando el usuario presiona el botón "Finalizar Pago"
    formularioPago.addEventListener("submit", function(evento) {
        evento.preventDefault(); // Evita que la página se recargue

        // Verificamos que todos los campos estén completos
        if (campoNombre.value === "" || campoApellido.value === "" || campoDni.value === "" ||
            campoDireccion.value === "" || campoNumeroTarjeta.value === "" || 
            campoNombreTarjeta.value === "" || campoVencimiento.value === "" || 
            campoCvv.value === "") {

            
            return; // detenemos el proceso si falta algo
        }

        // Validación simple del número de tarjeta
        if (campoNumeroTarjeta.value.length < 16) {
            
            return;
        }

        // Si está todo bien, mostramos mensaje de éxito
        formularioPago.style.display = "none";
        mensajeExito.classList.remove("oculto");

        // Guardamos los datos básicos del usuario (simulación)
        var datosUsuario = {
            nombre: campoNombre.value,
            apellido: campoApellido.value,
            dni: campoDni.value,
            direccion: campoDireccion.value
        };

    });

});
