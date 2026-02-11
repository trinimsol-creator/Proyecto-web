document.getElementById("Myform").addEventListener("submit", enviarFormulario);

function enviarFormulario(event) {

    const mensaje = document.getElementById("mensaje");
    const mensaje1 = document.getElementById("mensaje1");
    const mensaje2 = document.getElementById("mensaje2");
    const mensaje3 = document.getElementById("mensaje3");
    const mensaje4 = document.getElementById("mensaje4");
    const mensaje5 = document.getElementById("mensaje5");

    mensaje.textContent = "";
    mensaje1.textContent = "";
    mensaje2.textContent = "";
    mensaje3.textContent = "";
    mensaje4.textContent = "";
    mensaje5.textContent = "";


    const nombre = document.getElementById("nombre").value.trim();
    const precio = document.getElementById("precio").value.trim();
    const detalles = document.getElementById("detalles").value.trim();
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');
    const selLoc = document.getElementById("selLoc").value;

    let valido = true;
    const regex = /^[a-zA-Z0-9\s.,-]+$/;

    if (!nombre || !precio || !detalles || !colorSeleccionado || !selLoc) {
        if (mensaje) {
            mensaje.classList.add("error");
            mensaje.textContent = "Por favor, complete todos los campos.";
        }
        valido = false;
    }

    
    if (!nombre) {
        if (mensaje1) {
            mensaje1.textContent = "El nombre no puede estar vacío.";
            mensaje1.classList.add("error");
        }
        valido = false;
    } else if (!regex.test(nombre)) {
        if (mensaje1) {
            mensaje1.textContent = "El nombre contiene caracteres no válidos.";
            mensaje1.classList.add("error");
        }
        valido = false;
    }

    const precioNum = parseFloat(precio);
    if (isNaN(precioNum)) {
        if (mensaje2) {
            mensaje2.textContent = "El precio debe ser un número.";
            mensaje2.classList.add("error");
        }
        valido = false;
    } else if (precioNum <= 0) {
        if (mensaje2) {
            mensaje2.textContent = "El precio debe ser positivo.";
            mensaje2.classList.add("error");
        }
        valido = false;
    }

    if (!detalles) {
        if (mensaje3) {
            mensaje3.textContent = "Los detalles no pueden estar vacíos.";
            mensaje3.classList.add("error");
        }
        valido = false;
    } else if (!regex.test(detalles)) {
        if (mensaje3) {
            mensaje3.textContent = "Los detalles contienen caracteres no válidos.";
            mensaje3.classList.add("error");
        }
        valido = false;
    }

    if (!colorSeleccionado) {
        if (mensaje4) {
            mensaje4.textContent = "Seleccione un color.";
            mensaje4.classList.add("error");
        }
        valido = false;
    }

    if (!selLoc) {
        if (mensaje5) {
            mensaje5.textContent = "Seleccione una categoría.";
            mensaje5.classList.add("error");
        }
        valido = false;
    }

    if (!valido) {
        event.preventDefault();  
        return;
    }

    if (mensaje) {
        mensaje.textContent = "Producto validado, enviando...";
        mensaje.classList.add("exito");
    }

    
}
