const form = document.querySelector('form');
form.addEventListener('submit', function(event) {

    event.preventDefault(); 

    
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
    }

    
    if (password.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres.');
        return;
    }
   
    window.location.href = '../Pag Principal/PPrincipal.html';

});
