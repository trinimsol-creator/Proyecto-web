document.addEventListener("DOMContentLoaded", function() {
  const botonesEliminar = document.getElementsByClassName("remove-btn");
  const cantidades = document.querySelectorAll(".quantity input");
  const totalElement = document.querySelector(".total-card h2");
  const totalDescuentoElement = document.querySelector(".discount-total");

  // Función para formatear números como moneda
  function formatearPrecio(valor) {
    return "$" + valor.toLocaleString("es-AR");
  }

  // Función para recalcular el total
  function recalcularTotal() {
    let total = 0;
    let totalDescuento = 0;

    const productos = document.querySelectorAll(".product-card");
    productos.forEach(producto => {
      if (producto.style.display !== "none") {
        const precioTexto = producto.querySelector(".price").innerText.replace("$", "").replace(/\./g, "");
        const precio = parseInt(precioTexto);

        const descuentoTexto = producto.querySelector(".discount").innerText.replace(/[^0-9]/g, "");
        const descuento = parseInt(descuentoTexto);

        const cantidad = parseInt(producto.querySelector(".quantity input").value);

        total += precio * cantidad;
        totalDescuento += descuento * cantidad;
      }
    });

    totalElement.innerText = `Total: ${formatearPrecio(total)}`;
    totalDescuentoElement.innerText = `Total con descuento por transferencia bancaria: ${formatearPrecio(totalDescuento)}`;
  }

  // Evento para eliminar producto
  for (let i = 0; i < botonesEliminar.length; i++) {
    botonesEliminar[i].addEventListener("click", function() {
      const tarjetaProducto = this.parentElement;
      tarjetaProducto.style.display = "none";
      recalcularTotal();
    });
  }

  // Evento para actualizar al cambiar cantidades
  cantidades.forEach(input => {
    input.addEventListener("input", function() {
      if (this.value < 1) this.value = 1;
      recalcularTotal();
    });
  });

  // Calcular total inicial
  recalcularTotal();
});
