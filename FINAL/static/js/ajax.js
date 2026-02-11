function queryAjax(url, targetId = "", method = "POST", data = null) {
  const xhr = new XMLHttpRequest();

  xhr.open(method, url, true);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {

      if (xhr.status === 200) {
        if (targetId) {
          document.getElementById(targetId).innerHTML = xhr.responseText;
        }
      } else {
        console.error("Error AJAX:", xhr.status, xhr.responseText);
        alert("Ocurrió un error al comunicarse con el servidor.");
      }

    }
  };

  xhr.send(data);
}

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

function agregarCarrito(idProducto) {
  const cantidad = document.getElementById("cantidad").value;

  let data = new FormData();
  data.append("id", idProducto);
  data.append("cantidad", cantidad);

  queryAjax("/ajax/agregar_carrito", "", "POST", data);

  mostrarToast("Producto agregado al carrito");
}

function mostrarToast(texto) {
  const toast = document.createElement("div");
  toast.className = "toast-msg";
  toast.innerText = texto;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("show");
  }, 10);

  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}
