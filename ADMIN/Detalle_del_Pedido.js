document.addEventListener("DOMContentLoaded", function() {

  
    var selectorEstadoPedido = document.getElementById("estado1");
    var botonGuardarEstado = document.getElementById("btn-guardar");
    var tituloPedido = document.querySelector("h2");

  
    var textoPedido = tituloPedido.textContent;
    var numeroPedido = textoPedido.match(/\d+/)[0]; 
    var claveLocalStorage = "estado_" + numeroPedido; 

 
    var estadoGuardado = localStorage.getItem(claveLocalStorage);
    if (estadoGuardado) {
        selectorEstadoPedido.value = estadoGuardado;
    }

   
    botonGuardarEstado.addEventListener("click", function() {

        
        var estadoActual = selectorEstadoPedido.value;

        
        localStorage.setItem(claveLocalStorage, estadoActual);

        
        mostrarMensajeToast("✅ Pedido " + numeroPedido + " actualizado a: " + estadoActual);

      
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
