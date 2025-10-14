document.addEventListener("DOMContentLoaded", function() {

    // 1️⃣ Seleccionamos los elementos del HTML que vamos a usar
    var selectorEstadoPedido = document.getElementById("estado1");
    var botonGuardarEstado = document.getElementById("btn-guardar");
    var tituloPedido = document.querySelector("h2");

    // 2️⃣ Extraemos el número del pedido desde el texto (por ejemplo, "Pedido #1027")
    var textoPedido = tituloPedido.textContent;
    var numeroPedido = textoPedido.match(/\d+/)[0]; // extrae el número
    var claveLocalStorage = "estado_" + numeroPedido; // ejemplo: "estado_1027"

    // 3️⃣ Si existe un estado guardado, lo mostramos al cargar la página
    var estadoGuardado = localStorage.getItem(claveLocalStorage);
    if (estadoGuardado) {
        selectorEstadoPedido.value = estadoGuardado;
    }

    // 4️⃣ Agregamos el evento al botón para guardar el nuevo estado
    botonGuardarEstado.addEventListener("click", function() {

        // Obtenemos el estado seleccionado actualmente
        var estadoActual = selectorEstadoPedido.value;

        // Guardamos el estado en localStorage para que se mantenga
        localStorage.setItem(claveLocalStorage, estadoActual);

        // Mostramos un pequeño mensaje visual al usuario
        mostrarMensajeToast("✅ Pedido " + numeroPedido + " actualizado a: " + estadoActual);

        // Cambiamos el color del botón según el estado actual
        if (estadoActual.indexOf("Pendiente") !== -1) {
            botonGuardarEstado.style.background = "#888";
        } else if (estadoActual.indexOf("preparación") !== -1) {
            botonGuardarEstado.style.background = "#f7b731";
        } else if (estadoActual.indexOf("Listo") !== -1) {
            botonGuardarEstado.style.background = "#1e90ff";
        } else if (estadoActual.indexOf("Entregado") !== -1) {
            botonGuardarEstado.style.background = "#2ecc71";
        } else {
            botonGuardarEstado.style.background = "#222";
        }
    });

    // 5️⃣ Función tradicional para mostrar un mensaje visual tipo "toast"
    function mostrarMensajeToast(texto) {
        var nuevoToast = document.createElement("div");
        nuevoToast.classList.add("toast");
        nuevoToast.textContent = texto;
        document.body.appendChild(nuevoToast);

        // Efecto de aparición (fade in)
        setTimeout(function() {
            nuevoToast.style.opacity = "1";
        }, 100);

        // Efecto de desaparición (fade out)
        setTimeout(function() {
            nuevoToast.style.opacity = "0";
            setTimeout(function() {
                nuevoToast.remove();
            }, 500);
        }, 2500);
    }

});
