document.getElementById("Myform").addEventListener("submit", form);

function form(event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const precio = document.getElementById("precio").value;
    const detalles = document.getElementById("detalles").value;
    const selLoc = document.getElementById("selLoc").value;
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');

    mensaje.style.color = "red";

    if (nombre === "" || precio === "" || detalles === "" || !colorSeleccionado) {
        mensaje.textContent = "Por favor, complete todos los campos.";
        return;
    }

    if (precio <= 0) {
        mensaje2.textContent = "El precio debe ser un número positivo.";
        return;
    }
        const regex = /^[a-zA-Z0-9\s.,-]+$/;
    if (!regex.test(nombre) || !regex.test(detalles)) {
        mensaje1.textContent = "El nombre y los detalles solo pueden contener letras, números, espacios y algunos caracteres especiales (.,-).";
        return;
    }

    if (detalles === "") {
        mensaje3.textContent = "Los detalles no pueden estar vacíos.";
        return;
    }



    window.location.href = "../pagAdmin/pagAdmin.html";

};