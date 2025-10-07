const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    // Evita que el formulario se envíe por defecto
    event.preventDefault(); 

    // Obtener los valores de los campos
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    // 1. Validar el formato del correo electrónico
    // Esta expresión regular es una forma simple de verificar si el email tiene un formato básico correcto
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
    }

    // 2. Validar la longitud de la contraseña
    if (password.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres.');
        return;
    }
    // Si todas las validaciones pasan, se puede proceder a enviar el formulario
    //alert('Formulario validado con éxito. ¡Listo para iniciar sesión!');
    window.location.href = '../Pag Principal/PPrincipal.html';

});
