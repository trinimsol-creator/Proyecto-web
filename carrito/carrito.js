document.addEventListener("DOMContentLoaded", function () {
  
  var botonesEliminar = document.getElementsByClassName("remove-btn");
  var cantidades = document.querySelectorAll(".quantity input");
  var totalElement = document.querySelector(".total-card h2");
  var totalDescuentoElement = document.querySelector(".discount-total");

  function formatearPrecio(valor) {
    return "$" + valor.toLocaleString("es-AR");
  }

  function recalcularTotal() {
    var total = 0;
    var totalDescuento = 0;

    var productos = document.querySelectorAll(".product-card");

    productos.forEach(function (producto) {
      if (producto.style.display !== "none") {
        var precioTexto = producto.querySelector(".price").innerText.replace("$", "").replace(/\./g, "");
        var precio = parseInt(precioTexto);

        var descuentoTexto = producto.querySelector(".discount").innerText.replace(/[^0-9]/g, "");
        var descuento = parseInt(descuentoTexto);

        var cantidad = parseInt(producto.querySelector(".quantity input").value);

        total += precio * cantidad;
        totalDescuento += descuento * cantidad;
      }
    });

    totalElement.innerText = "Total: " + formatearPrecio(total);
    totalDescuentoElement.innerText =
      "Total con descuento por transferencia bancaria: " + formatearPrecio(totalDescuento);
  }

  for (var i = 0; i < botonesEliminar.length; i++) {
    botonesEliminar[i].addEventListener("click", function () {
      var tarjetaProducto = this.parentElement;
      tarjetaProducto.style.display = "none";
      recalcularTotal();
    });
  }

 
  cantidades.forEach(function (input) {
    input.addEventListener("input", function () {
      if (this.value < 1) {
        this.value = 1;
      }
      recalcularTotal();
    });
  });

  recalcularTotal();
});
