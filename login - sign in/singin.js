document.getElementById("Signin").addEventListener("submit", Signin);

function limpiarMensajes() {
  document.getElementById("msg-name").textContent = "";
  document.getElementById("msg-email").textContent = "";
  document.getElementById("msg-pass").textContent = "";
  document.getElementById("msg-confirm").textContent = "";
  document.getElementById("msg-global").textContent = "";
}

function Signin(event) {
  event.preventDefault();
  limpiarMensajes();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;

  let hayError = false;

  if (name === "" || email === "" || password === "" || confirmPassword === "") {
    document.getElementById("msg-global").textContent = "Por favor, complete todos los campos.";
    hayError = true;
  }

  if (name === "") {
    document.getElementById("msg-name").textContent = "Ingresá tu nombre de usuario.";
    hayError = true;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === "" || !emailRegex.test(email)) {
    document.getElementById("msg-email").textContent = "Ingresá un correo electrónico válido.";
    hayError = true;
  }

  if (password.length < 6) {
    document.getElementById("msg-pass").textContent = "La contraseña debe tener al menos 6 caracteres.";
    hayError = true;
  }

  if (password !== confirmPassword) {
    document.getElementById("msg-confirm").textContent = "Las contraseñas no coinciden.";
    hayError = true;
  }

  if (hayError) return;

  window.location.href = "../Pag Principal/PPrincipal.html";
}
