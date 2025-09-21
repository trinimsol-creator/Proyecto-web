let valorContador = 1;
function pintar(){ document.getElementById('contador').textContent = valorContador; }
function incrementar(){ valorContador++; pintar(); }
function decrementar(){ if (valorContador > 1) { valorContador--; pintar(); } }
