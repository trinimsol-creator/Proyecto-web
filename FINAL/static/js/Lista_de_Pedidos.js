document.addEventListener("DOMContentLoaded", function() {

   
    var listaDePedidos = document.querySelectorAll(".pedido");

    
    for (var i = 0; i < listaDePedidos.length; i++) {
        var pedidoActual = listaDePedidos[i];

        var textoPedido = pedidoActual.querySelector("h3").textContent;
        var numeroPedido = textoPedido.match(/\d+/)[0];
        var claveLocalStorage = "estado_" + numeroPedido;

        var estadoGuardado = localStorage.getItem(claveLocalStorage);
        if (estadoGuardado) {
            var parrafos = pedidoActual.querySelectorAll("p");
            for (var j = 0; j < parrafos.length; j++) {
                if (parrafos[j].textContent.indexOf("Estado:") !== -1) {
                    parrafos[j].innerHTML = "<b>Estado:</b> " + estadoGuardado;
                }
            }
        }

        
        pedidoActual.addEventListener("mouseenter", function() {
            this.style.transform = "scale(1.03)";
        });

        pedidoActual.addEventListener("mouseleave", function() {
            this.style.transform = "scale(1)";
        });
    }
});
