document.getElementById("Login").addEventListener("submit", onLogin);

function limpiarMensajes() {
  document.getElementById("mensaje1").textContent = "";
  document.getElementById("mensaje2").textContent = "";
  document.getElementById("mensaje3").textContent = "";
}

function onLogin(event) {
  event.preventDefault();
  limpiarMensajes();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  let valido = true;

  // Mensaje global si falta algo
  if (email === "" || password === "") {
    document.getElementById("mensaje3").textContent = "Completá email y contraseña.";
    valido = false;
  }

  // Email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === "" || !emailRegex.test(email)) {
    document.getElementById("mensaje1").textContent = "Ingresá un correo electrónico válido.";
    valido = false;
  }

  // Password
  if (password.length < 6) {
    document.getElementById("mensaje2").textContent = "La contraseña debe tener al menos 6 caracteres.";
    valido = false;
  }

  if (!valido) return;

  // Éxito
  window.location.href = "../Pag Principal/PPrincipal.html";
}
