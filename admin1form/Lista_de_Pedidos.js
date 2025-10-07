// ====== LISTA_DE_PEDIDOS.JS ======
// Archivo sencillo con comentarios paso a paso
// Actualiza los estados de los pedidos guardados desde el Detalle
// y agrega una barra de búsqueda funcional.

document.addEventListener("DOMContentLoaded", function() {
  // 1️⃣ Seleccionamos todos los pedidos y el input de búsqueda
  const pedidos = document.querySelectorAll(".pedido");
  const buscar = document.getElementById("buscar");

  // 2️⃣ Recorremos cada pedido y actualizamos su estado si fue cambiado antes
  pedidos.forEach(function(pedido) {
    // Extraemos el número del pedido
    const texto = pedido.querySelector("h3").textContent;
    const numero = texto.match(/\d+/)[0];
    const clave = "estado_" + numero;

    // Si hay un estado guardado en localStorage, lo mostramos
    const guardado = localStorage.getItem(clave);
    if (guardado) {
      const pEstado = Array.from(pedido.querySelectorAll("p")).find(p => p.textContent.includes("Estado:"));
      if (pEstado) pEstado.innerHTML = "<b>Estado:</b> " + guardado;
    }

    // 3️⃣ Efecto visual al pasar el mouse
    pedido.addEventListener("mouseenter", function() {
      pedido.style.transform = "scale(1.03)";
    });
    pedido.addEventListener("mouseleave", function() {
      pedido.style.transform = "scale(1)";
    });
  });

  // 4️⃣ Función de búsqueda en tiempo real
  buscar.addEventListener("input", function() {
    const query = buscar.value.toLowerCase();

    pedidos.forEach(function(pedido) {
      const textoPedido = pedido.textContent.toLowerCase();
      // Si coincide con el texto, lo mostramos, sino lo ocultamos
      if (textoPedido.includes(query)) {
        pedido.style.display = "block";
      } else {
        pedido.style.display = "none";
      }
    });
  });
});
