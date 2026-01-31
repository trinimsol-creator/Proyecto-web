document.getElementById("Myform").addEventListener("submit", form);

function form(event) {
    event.preventDefault();

    mensaje.textContent = "";
    mensaje1.textContent = "";
    mensaje2.textContent = "";
    mensaje3.textContent = "";
    mensaje4.textContent = "";
    mensaje5.textContent = "";

    const nombre = document.getElementById("nombre").value;
    const precio = document.getElementById("precio").value;
    const detalles = document.getElementById("detalles").value;
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');
    const selLoc = document.getElementById("selLoc").value;

    mensaje.style.color = "red";

    let valido = true;

    if (nombre === "" || precio === "" || detalles === "" || !colorSeleccionado) {
        mensaje.textContent = "Por favor, complete todos los campos.";
        valido = false;
    }

  
    const regex = /^[a-zA-Z0-9\s.,-]+$/;
    if (nombre === "") {
        mensaje1.textContent = "El nombre no puede estar vacío.";
        valido = false;
    } else if (!regex.test(nombre) || !regex.test(detalles)) {
        mensaje1.textContent = "El nombre y los detalles solo pueden contener letras, números, espacios y algunos caracteres especiales (.,-).";
        valido = false;
    }


    if (precio === "") {
        mensaje2.textContent = "El precio no puede estar vacío.";
        valido = false;
    } else if (precio <= 0) {
        mensaje2.textContent = "El precio debe ser un número positivo.";
        valido = false;
    }


    if (detalles === "") {
        mensaje3.textContent = "Los detalles no pueden estar vacíos.";
        valido = false;
    }



    if (selLoc === "") {
        mensaje5.textContent = "Por favor, seleccione una categoría.";
        valido = false;
    }



    if (!colorSeleccionado) {
        mensaje4.textContent = "Por favor, seleccione un color.";
        valido = false;
    }

    if (!valido) return;
    mensaje.style.color = "green";
    mensaje.textContent = "Producto creado con éxito.";
    
    setTimeout(() => {
        window.location.href = "pagAdmin.html";
    }, 3000);
};