document.getElementById("formularioPago").addEventListener("submit", form);

function form(event) {
  event.preventDefault();

  const nombreUsuario = document.getElementById("nombreUsuario").value.trim();
  const apellidoUsuario = document.getElementById("apellidoUsuario").value.trim();
  const dniUsuario = document.getElementById("dniUsuario").value.trim();
  const cvuTarjeta = document.getElementById("cvuTarjeta").value.trim();
  const direccionUsuario = document.getElementById("direccionUsuario").value.trim();
  const comprobante = document.getElementById("Comprobante").value.trim();

  let valido = true;

  mensaje.textContent = "";
  mensaje1.textContent = "";
  mensaje2.textContent = "";
  mensaje3.textContent = "";
  mensaje4.textContent = "";
  mensaje5.textContent = "";
  mensaje6.textContent = "";

 
  if (nombreUsuario === "" || apellidoUsuario === "" || dniUsuario === "" || cvuTarjeta === "" || comprobante === "" || direccionUsuario === "") {
    mensaje.textContent = "Por favor, complete todos los campos.";
    valido = false;
  }

 
  const nombreRegex = /^[a-zA-Z\s]+$/;
if (nombreUsuario === "") {
    mensaje1.textContent = "Por favor, ingrese su nombre.";
    valido = false;
  } else if (!nombreRegex.test(nombreUsuario) ) {
    mensaje1.textContent = "El nombre solo puede contener letras y espacios.";
    valido = false;
  }


  if (apellidoUsuario === "") {
    mensaje2.textContent = "Por favor, ingrese su apellido.";
    valido = false;
  } else if (!nombreRegex.test(apellidoUsuario)) {
    mensaje2.textContent = "El apellido solo puede contener letras y espacios.";
    valido = false;
  }


  
  if (dniUsuario.length !== 8) {
    mensaje3.textContent = "El DNI debe tener 8 dígitos.";
    valido = false;
  } else if (!/^[0-9]+$/.test(dniUsuario)) {
    mensaje3.textContent = "El DNI solo puede contener números.";
    valido = false;
  }


  if (cvuTarjeta.length !== 22) {
    mensaje4.textContent = "El CVU debe tener 22 dígitos.";
    valido = false;
  } else if (!/^[0-9]+$/.test(cvuTarjeta)) {
    mensaje4.textContent = "El CVU solo puede contener números.";
    valido = false;
  }

  if (direccionUsuario === "") {
    mensaje6.textContent = "Por favor, ingrese una dirección.";
    valido = false;
  }

  if (!comprobante) {
    mensaje5.textContent = "Por favor, suba el comprobante.";
    valido = false;
  }

  if (valido) {
    window.location.href = "/";
  }
}
