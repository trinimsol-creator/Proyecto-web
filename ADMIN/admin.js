


var formularioInicioSesion = document.getElementById("login-form");
var pantallaLogin = document.getElementById("login-screen");
var panelAdministrador = document.getElementById("admin-panel");
var botonCerrarSesion = document.getElementById("logout-btn");

formularioInicioSesion.addEventListener("submit", function(evento) {
    
    evento.preventDefault();

    
    var correoIngresado = document.getElementById("email").value.trim();
    var contrasenaIngresada = document.getElementById("password").value.trim();

    
    if (correoIngresado === "admin@coast.com" && contrasenaIngresada === "1234") {
        
        pantallaLogin.classList.remove("active");
        pantallaLogin.classList.add("hidden");
        panelAdministrador.classList.remove("hidden");
    } else {
        
        alert("Correo o contraseña incorrectos");
    }
});


botonCerrarSesion.addEventListener("click", function() {
    
    panelAdministrador.classList.add("hidden");
    
    pantallaLogin.classList.remove("hidden");
    pantallaLogin.classList.add("active");
});


var botonesMenu = document.querySelectorAll(".menu-btn");
var marcosContenido = document.querySelectorAll(".content-frame");


function cambiarPestaniaActiva(botonSeleccionado) {
    var i; 
    for (i = 0; i < botonesMenu.length; i++) {
        botonesMenu[i].classList.remove("active");
    }
    botonSeleccionado.classList.add("active");
}


function mostrarContenidoAsociado(idDestino) {
    var j; 
    for (j = 0; j < marcosContenido.length; j++) {
        marcosContenido[j].classList.remove("active");
    }
    document.getElementById(idDestino).classList.add("active");
}


for (var i = 0; i < botonesMenu.length; i++) {
    botonesMenu[i].addEventListener("click", function() {
       
        var botonPresionado = this;
        
        cambiarPestaniaActiva(botonPresionado);
        
        var destino = botonPresionado.getAttribute("data-target");
        
        mostrarContenidoAsociado(destino);
    });
}