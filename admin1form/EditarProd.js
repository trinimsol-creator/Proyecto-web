document.getElementById("Myform").addEventListener("submit", form);

function form(event) {
    event.preventDefault();


    mensaje1.textContent = "";
    mensaje2.textContent = "";
    mensaje3.textContent = "";
    mensaje4.textContent = "";
    mensaje5.textContent = "";
    mensaje6.textContent = "";
    mensaje7.textContent = "";
    mensajeGlobal.textContent = "";


    const nombre = document.getElementById("nombre").value.trim();
    const precio = document.getElementById("precio").value.trim();
    const detalles = document.getElementById("detalles").value.trim();
    const stock = document.getElementById("selStock").value;
    const categoria = document.getElementById("selCategoria").value;
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');
    const archivo = document.getElementById("arch01").files[0];

    mensajeGlobal.style.color = "red";

    let valido = true;


    if (nombre === "" || precio === "" || detalles === "" || stock === "" || categoria === "" || !colorSeleccionado) {
        mensajeGlobal.textContent = "Por favor, completá todos los campos.";
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
    } else if (isNaN(precio) || precio <= 0) {
        mensaje2.textContent = "El precio debe ser un número positivo.";
        valido = false;
    }

    if (detalles === "") {
        mensaje3.textContent = "Los detalles no pueden estar vacíos.";
        valido = false;
    }


    if (stock === "") {
        mensaje4.textContent = "Seleccioná el estado de stock.";
        valido = false;
    }


    if (categoria === "") {
        mensaje5.textContent = "Seleccioná una categoría.";
        valido = false;
    }


    if (!colorSeleccionado) {
        mensaje6.textContent = "Elegí un color.";
        valido = false;
    }


    if (!valido) return;
    mensaje.style.color = "green";
    mensaje.textContent = "Producto creado con éxito.";
    window.location.href = "file:///C:/Users/lenovo/Documents/GitHub/Proyecto-web/ADMIN/admin.html";
}