document.getElementById("Myform").addEventListener("submit", enviarFormulario);

function enviarFormulario(event) {

    const mensaje = document.getElementById("mensaje");
    const mensaje1 = document.getElementById("mensaje1");
    const mensaje2 = document.getElementById("mensaje2");
    const mensaje3 = document.getElementById("mensaje3");
    const mensaje4 = document.getElementById("mensaje4");
    const mensaje5 = document.getElementById("mensaje5");

    [mensaje, mensaje1, mensaje2, mensaje3, mensaje4, mensaje5].forEach(m => {
        if (m) m.textContent = "";
    });

    const nombre = document.getElementById("nombre").value.trim();
    const precio = document.getElementById("precio").value.trim();
    const detalles = document.getElementById("detalles").value.trim();
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');
    const selLoc = document.getElementById("selLoc").value;

    let valido = true;

    if (!nombre || !precio || !detalles || !colorSeleccionado || !selLoc) {
        if (mensaje) {
            mensaje.style.color = "red";
            mensaje.textContent = "Por favor, complete todos los campos.";
        }
        valido = false;
    }

    const regex = /^[a-zA-Z0-9\s.,-]+$/;

    if (!nombre) {
        if (mensaje1) mensaje1.textContent = "El nombre no puede estar vacío.";
        valido = false;
    } else if (!regex.test(nombre)) {
        if (mensaje1) mensaje1.textContent = "El nombre contiene caracteres no válidos.";
        valido = false;
    }

    const precioNum = parseFloat(precio);
    if (isNaN(precioNum)) {
        if (mensaje2) mensaje2.textContent = "El precio debe ser un número.";
        valido = false;
    } else if (precioNum <= 0) {
        if (mensaje2) mensaje2.textContent = "El precio debe ser positivo.";
        valido = false;
    }

    if (!detalles) {
        if (mensaje3) mensaje3.textContent = "Los detalles no pueden estar vacíos.";
        valido = false;
    } else if (!regex.test(detalles)) {
        if (mensaje3) mensaje3.textContent = "Los detalles contienen caracteres no válidos.";
        valido = false;
    }

    if (!colorSeleccionado) {
        if (mensaje4) mensaje4.textContent = "Seleccione un color.";
        valido = false;
    }

    if (!selLoc) {
        if (mensaje5) mensaje5.textContent = "Seleccione una categoría.";
        valido = false;
    }

    if (!valido) {
        event.preventDefault();  // bloquea el envío si hay errores
        return;
    }

    if (mensaje) {
        mensaje.style.color = "green";
        mensaje.textContent = "Producto validado, enviando...";
    }

    // 🔴 NO usamos preventDefault() → el form se envía normal a Flask
}
