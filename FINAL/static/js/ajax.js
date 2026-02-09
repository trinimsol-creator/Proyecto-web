document.addEventListener("DOMContentLoaded", () => {

  document.querySelectorAll(".cantidad").forEach(input => {
    input.addEventListener("change", cambiarCantidad);
  });

  document.querySelectorAll(".remove-btn").forEach(btn => {
    btn.addEventListener("click", eliminarProducto);
  });

});

function cambiarCantidad(e) {
  const card = e.target.closest(".product-card");
  const idProducto = card.dataset.id;
  const cantidad = e.target.value;

  let data = new FormData();
  data.append("id", idProducto);
  data.append("cantidad", cantidad);

  queryAjax("/ajax/actualizar_carrito", "total-carrito", "POST", data);
}

function eliminarProducto(e) {
  const card = e.target.closest(".product-card");
  const idProducto = card.dataset.id;

  let data = new FormData();
  data.append("id", idProducto);

  queryAjax("/ajax/eliminar_producto", "total-carrito", "POST", data);

  card.remove();
}

