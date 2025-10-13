/*PANEL DE ADMINISTRACIÓN - TIENDA COAST(sin funciones flecha)*/

/* ======= LOGIN ======= */

// Guardo los elementos importantes en variables con nombres descriptivos y claros
var formularioInicioSesion = document.getElementById("login-form");
var pantallaLogin = document.getElementById("login-screen");
var panelAdministrador = document.getElementById("admin-panel");
var botonCerrarSesion = document.getElementById("logout-btn");

// Esta función se ejecuta cuando el usuario hace clic en "Iniciar Sesión"
formularioInicioSesion.addEventListener("submit", function(evento) {
    // Evita que el formulario recargue la página
    evento.preventDefault();

    // Obtengo los valores escritos en los campos
    var correoIngresado = document.getElementById("email").value.trim();
    var contrasenaIngresada = document.getElementById("password").value.trim();

    // Compruebo si el correo y la contraseña son correctos
    if (correoIngresado === "admin@coast.com" && contrasenaIngresada === "1234") {
        // Si los datos son correctos, muestro el panel y oculto el login
        pantallaLogin.classList.remove("active");
        pantallaLogin.classList.add("hidden");
        panelAdministrador.classList.remove("hidden");
    } else {
        // Si no coinciden, aviso al usuario
        alert("Correo o contraseña incorrectos");
    }
});

/* ======= CERRAR SESIÓN ======= */

// Esta función vuelve al login cuando se hace clic en "Cerrar Sesión"
botonCerrarSesion.addEventListener("click", function() {
    // Oculto el panel del administrador
    panelAdministrador.classList.add("hidden");
    // Vuelvo a mostrar la pantalla de login
    pantallaLogin.classList.remove("hidden");
    pantallaLogin.classList.add("active");
});

/* ======= MENÚ LATERAL ======= */

// Guardo en variables todos los botones del menú y los iframes del contenido
var botonesMenu = document.querySelectorAll(".menu-btn");
var marcosContenido = document.querySelectorAll(".content-frame");

// Esta función cambia la pestaña activa del panel
function cambiarPestaniaActiva(botonSeleccionado) {
    var i; // índice para recorrer los botones
    for (i = 0; i < botonesMenu.length; i++) {
        botonesMenu[i].classList.remove("active");
    }
    botonSeleccionado.classList.add("active");
}

// Esta función muestra el iframe correspondiente al botón presionado
function mostrarContenidoAsociado(idDestino) {
    var j; // índice para recorrer los iframes
    for (j = 0; j < marcosContenido.length; j++) {
        marcosContenido[j].classList.remove("active");
    }
    document.getElementById(idDestino).classList.add("active");
}

// Recorro todos los botones y les agrego el clic
for (var i = 0; i < botonesMenu.length; i++) {
    botonesMenu[i].addEventListener("click", function() {
        // Obtengo el botón que fue presionado
        var botonPresionado = this;
        // Cambio la pestaña activa visualmente
        cambiarPestaniaActiva(botonPresionado);
        // Busco el id del iframe que le corresponde
        var destino = botonPresionado.getAttribute("data-target");
        // Muestro ese iframe
        mostrarContenidoAsociado(destino);
    });
}