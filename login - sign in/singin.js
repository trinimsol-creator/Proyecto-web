document.getElementById("Signin").addEventListener("submit", Signin);


function Signin(event) {
    event.preventDefault(); 

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (name === '' || email === '' || password === '' || confirmPassword === '') {
        alert('Por favor, complete todos los campos.');
            return;
    }
    
    if (name === '') {
        alert('Por favor, ingresa tu nombre de usuario.');
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
    }

    if (password.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres.');
        return;
    }

    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden. Por favor, revísalas.');
        return;
    }

    window.location.href = '../Pag Principal/PPrincipal.html';
};
