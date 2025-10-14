

document.addEventListener("DOMContentLoaded", function() {

  const pedidos = document.querySelectorAll(".pedido");
  const buscar = document.getElementById("buscar");

  
  pedidos.forEach(function(pedido) {
  
    const texto = pedido.querySelector("h3").textContent;
    const numero = texto.match(/\d+/)[0];
    const clave = "estado_" + numero;

    
    const guardado = localStorage.getItem(clave);
    if (guardado) {
      const pEstado = Array.from(pedido.querySelectorAll("p")).find(p => p.textContent.includes("Estado:"));
      if (pEstado) pEstado.innerHTML = "<b>Estado:</b> " + guardado;
    }

    
    pedido.addEventListener("mouseenter", function() {
      pedido.style.transform = "scale(1.03)";
    });
    pedido.addEventListener("mouseleave", function() {
      pedido.style.transform = "scale(1)";
    });
  });

  
  buscar.addEventListener("input", function() {
    const query = buscar.value.toLowerCase();

    pedidos.forEach(function(pedido) {
      const textoPedido = pedido.textContent.toLowerCase();
      
      if (textoPedido.includes(query)) {
        pedido.style.display = "block";
      } else {
        pedido.style.display = "none";
      }
    });
  });
});
