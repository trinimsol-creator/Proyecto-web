document.getElementById("Myform").addEventListener("submit", onSubmit);

const M1 = id => document.getElementById(id);
function limpiar() {
  ["mensaje1","mensaje2","mensaje3","mensaje4","mensaje5","mensaje6","mensaje7","mensajeGlobal"]
    .forEach(id => M1(id).textContent = "");
}

function onSubmit(e){
  e.preventDefault();
  limpiar();

  const nombre = M1("nombre").value.trim();
  const precio = parseFloat(M1("precio").value);
  const detalles = M1("detalles").value.trim();
  const stock = M1("selStock").value;
  const categoria = M1("selCategoria").value;
  const color = document.querySelector('input[name="color"]:checked');
  const archivo = M1("arch01").files[0];

  let ok = true;

  if (!nombre || !detalles || isNaN(precio) || !stock || !categoria || !color) {
    M1("mensajeGlobal").textContent = "Por favor, completá todos los campos.";
    ok = false;
  }

  if (!nombre) {
    M1("mensaje1").textContent = "Ingresá el nombre del producto.";
    ok = false;
  }

  if (isNaN(precio) || precio <= 0) {
    M1("mensaje2").textContent = "El precio debe ser un número positivo.";
    ok = false;
  }

  const regex = /^[a-zA-Z0-9\s.,-]+$/;
  if (!detalles || !regex.test(detalles) || !regex.test(nombre)) {
    M1("mensaje3").textContent = "Sólo letras, números, espacios y . , -";
    ok = false;
  }

  if (!stock) {
    M1("mensaje4").textContent = "Seleccioná el estado de stock.";
    ok = false;
  }

  if (!categoria) {
    M1("mensaje5").textContent = "Seleccioná una categoría.";
    ok = false;
  }

  if (!color) {
    M1("mensaje6").textContent = "Elegí un color.";
    ok = false;
  }

  // opcional: validar archivo
  // if (!archivo) { M1("mensaje7").textContent = "Subí una foto."; ok = false; }

  if (!ok) return;

  // éxito
  window.location.href = "../admin1form/pagAdmin.html";
}