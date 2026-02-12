document.getElementById("formularioPago").addEventListener("submit", validarFormulario);
document.querySelectorAll('input[name="forma_pago"]').forEach(agregarEventListener);

function validarFormulario(event) {
    event.preventDefault();

    const metodoPago = document.querySelector('input[name="forma_pago"]:checked').value;
    
    if (metodoPago === "transferencia") {
        document.getElementById("formularioPago").submit();
        return;
    }

    const numero = document.getElementById("numero_tarjeta").value.trim();
    const nombre = document.getElementById("nombre_tarjeta").value.trim();
    const fecha = document.getElementById("fecha_tarjeta").value.trim();
    const codigo = document.getElementById("codigo_tarjeta").value.trim();

    const errorNumero = document.getElementById("error_numero");
    const errorNombre = document.getElementById("error_nombre");
    const errorFecha = document.getElementById("error_fecha");
    const errorCodigo = document.getElementById("error_codigo");

    errorNumero.textContent = "";
    errorNombre.textContent = "";
    errorFecha.textContent = "";
    errorCodigo.textContent = "";

    let esValido = true;

    const regexNumero = /^\d{16}$/;
    if (!regexNumero.test(numero)) {
        errorNumero.textContent = "El número de tarjeta debe tener 16 dígitos numéricos.";
        esValido = false;
    }

    if (nombre === "") {
        errorNombre.textContent = "El nombre es obligatorio.";
        esValido = false;
    }

    const regexFecha = /^(0[1-9]|1[0-2])\/\d{2}$/; // Formato MM/YY
    if (!regexFecha.test(fecha)) {
        errorFecha.textContent = "Formato inválido (MM/YY).";
        esValido = false;
    } else {
        const partes = fecha.split("/");
        const mes = parseInt(partes[0], 10);
        const anio = 2000 + parseInt(partes[1], 10);
        
        const fechaActual = new Date();
        const mesActual = fechaActual.getMonth() + 1;
        const anioActual = fechaActual.getFullYear();

        if (anio < anioActual || (anio === anioActual && mes < mesActual)) {
            errorFecha.textContent = "La tarjeta está vencida.";
            esValido = false;
        }
    }

    const regexCodigo = /^\d{3,4}$/;
    if (!regexCodigo.test(codigo)) {
        errorCodigo.textContent = "El código debe tener 3 o 4 dígitos.";
        esValido = false;
    }

    if (esValido) {
        document.getElementById("formularioPago").submit(); 
    }
}

function agregarEventListener(elem) {
  elem.addEventListener("change", changeEventListener);
}

function changeEventListener(event) {
  const metodo = event.target.value;
  const detallesTarjeta = document.getElementById("detalles_tarjeta");
  const detallesTransferencia = document.getElementById("detalles_transferencia");

  if (metodo === "tarjeta") {
      detallesTarjeta.classList.remove("oculto");
      detallesTransferencia.classList.add("oculto");
  } else {
      detallesTarjeta.classList.add("oculto");
      detallesTransferencia.classList.remove("oculto");
  }
}
