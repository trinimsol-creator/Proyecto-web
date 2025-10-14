document.getElementById("formularioPago").addEventListener("submit", pago);

function pago(event) {
    event.preventDefault();

    const nombreUsuario = document.getElementById("nombreUsuario").value.trim();
    const apellidoUsuario = document.getElementById("apellidoUsuario").value.trim();
    const dniUsuario = document.getElementById("dniUsuario").value.trim();
    const direccionUsuario = document.getElementById("direccionUsuario").value.trim();
    const cvuTarjeta = document.getElementById("cvuTarjeta").value.trim();

    mensaje.style.color = "red";
    

    if (nombreUsuario === "" || apellidoUsuario === "" || dniUsuario === "" || direccionUsuario === "" || cvuTarjeta === "") {
        mensaje.textContent = "Por favor, complete todos los campos.";
        return;
    }

    if (dniUsuario.length !== 8) {
        mensaje1.textContent = "El DNI debe tener 8 dígitos.";
        return;
    }

    if (cvuTarjeta.length !== 22) {
        mensaje2.textContent = "El CVU debe tener 22 dígitos.";
        return;
    }

    mensajeGeneral.style.color = "green";
    mensajeGeneral.textContent = "Formulario válido. Procesando pago...";
}
