document.getElementById("Signin").addEventListener("submit", onSignin);

function limpiarMensajes() {
  document.getElementById("msj_error_campo_incompleto").textContent = "";
  document.getElementById("msj_error_email_invalido").textContent = "";
  document.getElementById("msj_error_contrasenia_corta").textContent = "";
  document.getElementById("msj_error_contrasenia_no_coincide").textContent = "";
}

function onSignin(event) {
  event.preventDefault();
  limpiarMensajes();

  const usuario = {
    nombre_usuario:       document.getElementById("nombre_usuario").value.trim(),
    nombre:               document.getElementById("nombre").value.trim(),
    apellido:             document.getElementById("apellido").value.trim(),
    email:                document.getElementById("email").value.trim(),
    dni:                  document.getElementById("dni").value.trim(),
    direccion:            document.getElementById("direccion").value.trim(),
    password:             document.getElementById("password").value,
    confirm_password:     document.getElementById("confirm_password").value
  }

  let valid = true;
  
  /* Validacion de campos vacios */
  for (campo in usuario) {
    console.log(campo)
    console.log(usuario[campo])
    console.log(typeof usuario[campo])
    if (usuario[campo] === "") {
      document.getElementById("msj_error_campo_incompleto").textContent = "Por favor, completá todos los campos.";
      valid = false;
    }
  }

  /* Validacion de email */
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (usuario.email === "" || !emailRegex.test(usuario.email)) {
    document.getElementById("msj_error_email_invalido").textContent = "Ingresá un correo electrónico válido.";
    valid = false;
  }

  /* Validacion de largo minimo de contrasenia */
  if (usuario.password.length < 4) {
    document.getElementById("msj_error_contrasenia_corta").textContent = "La contraseña debe tener al menos 4 caracteres.";
    valid = false;
  }

  /* Validacion de que coincidan las contrasenias */
  if (usuario.password !== usuario.confirm_password) {
    document.getElementById("msj_error_contrasenia_no_coincide").textContent = "Las contraseñas no coinciden.";
    valid = false;
  }

  if (!valid) {
    return;
  }

  document.getElementById("Signin").submit();
}
