
document.addEventListener("DOMContentLoaded", function() {
  const selectEstado = document.getElementById("estado1");
  const botonGuardar = document.getElementById("btn-guardar");
  const tituloPedido = document.querySelector("h2");

  // Extraemos el número del pedido
  const numero = tituloPedido.textContent.match(/\d+/)[0];
  const clave = "estado_" + numero;

  // Al cargar la página, mostrar el estado guardado (si existe)
  const guardado = localStorage.getItem(clave);
  if (guardado) selectEstado.value = guardado;

  // Escuchamos el click del botón
  botonGuardar.addEventListener("click", function() {
    const estado = selectEstado.value;
    localStorage.setItem(clave, estado);

    // Mostramos un mensaje (toast)
    mostrarToast("✅ Pedido " + numero + " actualizado a: " + estado);

    // Cambiamos color del botón según el estado
    if (estado.includes("Pendiente")) botonGuardar.style.background = "#888";
    else if (estado.includes("preparación")) botonGuardar.style.background = "#f7b731";
    else if (estado.includes("Listo")) botonGuardar.style.background = "#1e90ff";
    else if (estado.includes("Entregado")) botonGuardar.style.background = "#2ecc71";
    else botonGuardar.style.background = "#222";
  });

  // Función para mostrar mensaje visual
  function mostrarToast(texto) {
    const toast = document.createElement("div");
    toast.classList.add("toast");
    toast.textContent = texto;
    document.body.appendChild(toast);

    // Fade in
    setTimeout(() => (toast.style.opacity = "1"), 100);

    // Desaparece después de 2.5s
    setTimeout(() => {
      toast.style.opacity = "0";
      setTimeout(() => toast.remove(), 500);
    }, 2500);
  }
});

