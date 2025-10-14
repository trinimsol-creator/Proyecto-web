document.addEventListener("DOMContentLoaded", function() {

   
    var listaDePedidos = document.querySelectorAll(".pedido");
    var campoBusqueda = document.getElementById("buscar");

    
    for (var i = 0; i < listaDePedidos.length; i++) {
        var pedidoActual = listaDePedidos[i];

        // Extraemos el número del pedido
        var textoPedido = pedidoActual.querySelector("h3").textContent;
        var numeroPedido = textoPedido.match(/\d+/)[0];
        var claveLocalStorage = "estado_" + numeroPedido;

        // Buscamos si hay un estado guardado y lo mostramos
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

    
    campoBusqueda.addEventListener("input", function() {
        var textoBuscado = campoBusqueda.value.toLowerCase();

        // Recorremos todos los pedidos para comparar
        for (var k = 0; k < listaDePedidos.length; k++) {
            var pedidoARevisar = listaDePedidos[k];
            var textoCompleto = pedidoARevisar.textContent.toLowerCase();

            if (textoCompleto.indexOf(textoBuscado) !== -1) {
                pedidoARevisar.style.display = "block";
            } else {
                pedidoARevisar.style.display = "none";
            }
        }
    });
});
