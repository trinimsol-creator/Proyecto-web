
document.addEventListener("DOMContentLoaded", function() {
  const selectEstado = document.getElementById("estado1");
  const botonGuardar = document.getElementById("btn-guardar");
  const tituloPedido = document.querySelector("h2");


  const numero = tituloPedido.textContent.match(/\d+/)[0];
  const clave = "estado_" + numero;

  
  const guardado = localStorage.getItem(clave);
  if (guardado) selectEstado.value = guardado;

  
  botonGuardar.addEventListener("click", function() {
    const estado = selectEstado.value;
    localStorage.setItem(clave, estado);

    
    mostrarToast("✅ Pedido " + numero + " actualizado a: " + estado);

    
    if (estado.includes("Pendiente")) botonGuardar.style.background = "#888";
    else if (estado.includes("preparación")) botonGuardar.style.background = "#f7b731";
    else if (estado.includes("Listo")) botonGuardar.style.background = "#1e90ff";
    else if (estado.includes("Entregado")) botonGuardar.style.background = "#2ecc71";
    else botonGuardar.style.background = "#222";
  });

  
  function mostrarToast(texto) {
    const toast = document.createElement("div");
    toast.classList.add("toast");
    toast.textContent = texto;
    document.body.appendChild(toast);

   
    setTimeout(() => (toast.style.opacity = "1"), 100);

    
    setTimeout(() => {
      toast.style.opacity = "0";
      setTimeout(() => toast.remove(), 500);
    }, 2500);
  }
});

