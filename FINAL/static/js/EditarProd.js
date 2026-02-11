document.getElementById("Myform").addEventListener("submit", form);
const mensaje  = document.getElementById("mensaje");

function form(event) {
    event.preventDefault();

    mensaje.textContent = "";

    mensaje.classList.remove("ok");
    mensaje.classList.remove("error");

    const nombre = document.getElementById("nombre").value;
    const precio = document.getElementById("precio").value;
    const detalles = document.getElementById("detalles").value;
    const colorSeleccionado = document.querySelector('input[name="color"]:checked');
    const selLoc = document.getElementById("selLoc").value;
    const estado = document.getElementById("estado").value;

    let valido = true;

    if (!nombre || !precio || !detalles || !colorSeleccionado || !selLoc || !estado) {
        mensaje.textContent = "Por favor, complete todos los campos.";
        mensaje.classList.add("error");
        valido = false;
    }

    if (!valido) return;

  
    mensaje.textContent = "Producto fue editado con éxito.";
    mensaje.classList.add("ok");

    event.target.removeEventListener("submit", form);
    event.target.submit();
}
