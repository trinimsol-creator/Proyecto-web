document.getElementById("Login").addEventListener("submit", onLogin);

function limpiarMensajes() {
  document.getElementById("mensaje1").textContent = "";
  document.getElementById("mensaje2").textContent = "";
  document.getElementById("mensaje3").textContent = "";
}

function onLogin(event) {
  event.preventDefault();
  limpiarMensajes();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  let valido = true;


  if (email === "" || password === "") {
    mensaje3.textContent = "Completá email y contraseña.";
    valido = false;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (email === "" || !emailRegex.test(email)) {
    mensaje1.textContent = "Ingresá un correo electrónico válido.";
    valido = false;
  }


  if (password.length < 6) {
    mensaje2.textContent = "La contraseña debe tener al menos 6 caracteres.";
    valido = false;
  }

  if (!valido) return;


  window.location.href = "../Pag Principal/PPrincipal.html";
}
