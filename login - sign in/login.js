document.getElementById("Login").addEventListener("submit", Login);

function Login(event) {
    event.preventDefault(); 

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();


    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === "" || !emailRegex.test(email)) {
        mensaje1.textContent = "Por favor, ingresa un correo electrónico válido.";
        valido = false;
    }

    if (password === "") {
        mensaje2.textContent = "La contraseña no puede estar vacía.";
        valido = false;
    } else if (password.length < 6) {
        mensaje2.textContent = "La contraseña debe tener al menos 6 caracteres.";
        valido = false;
    }

 window.location.href = "../Pag Principal/PPrincipal.html";
}
