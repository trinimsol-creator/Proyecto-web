document.getElementById("Signin").addEventListener("submit", onSignin);

function limpiarMensajes() {
  document.getElementById("mensaje1").textContent = "";
  document.getElementById("mensaje2").textContent = "";
  document.getElementById("mensaje3").textContent = "";
  document.getElementById("mensaje4").textContent = "";
  document.getElementById("mensaje5").textContent = "";
}

function onSignin(event) {
  event.preventDefault();
  limpiarMensajes();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;

  let valido = true;


  if (name === "" || email === "" || password === "" || confirmPassword === "") {
    document.getElementById("mensaje5").textContent = "Por favor, completá todos los campos.";
    valido = false;
  }


  if (name === "") {
    document.getElementById("mensaje1").textContent = "Ingresá tu nombre de usuario.";
    valido = false;
  }


  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === "" || !emailRegex.test(email)) {
    document.getElementById("mensaje2").textContent = "Ingresá un correo electrónico válido.";
    valido = false;
  }


  if (password.length < 6) {
    document.getElementById("mensaje3").textContent = "La contraseña debe tener al menos 6 caracteres.";
    valido = false;
  }


  if (password !== confirmPassword) {
    document.getElementById("mensaje4").textContent = "Las contraseñas no coinciden.";
    valido = false;
  }


  if (!valido) return;
  setTimeout(() => {
    window.location.href = "../Pag Principal/PPrincipal.html";
  }, 300);
}
