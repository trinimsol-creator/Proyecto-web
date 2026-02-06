document.getElementById("Myform").addEventListener("submit", form);
const mensaje  = document.getElementById("mensaje");
const mensaje1 = document.getElementById("mensaje1");
const mensaje2 = document.getElementById("mensaje2");
const mensaje3 = document.getElementById("mensaje3");
const mensaje4 = document.getElementById("mensaje4");
const mensaje5 = document.getElementById("mensaje5");
const mensaje6 = document.getElementById("mensaje6");


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
    const estado = document.getElementById("estado").value;

    let valido = true;

    if (!nombre || !precio || !detalles || !colorSeleccionado || !selLoc || !estado) {
        mensaje.textContent = "Por favor, complete todos los campos.";
        valido = false;
    }

    if (!valido) return;

    mensaje.style.color = "green";
    mensaje.textContent = "Producto fue editado con éxito.";

    event.target.removeEventListener("submit", form);
    event.target.submit();
}
