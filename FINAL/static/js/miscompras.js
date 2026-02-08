var botones = document.querySelectorAll(".filtros button"); 
var pedidos = document.querySelectorAll("#lista-pedidos .pedido");

function filtrar(tipo) {
 
  for (var i = 0; i < botones.length; i++) {
    botones[i].classList.remove("activo");
  }

  var boton = document.querySelector(".filtros button[onclick=\"filtrar('" + tipo + "')\"]");
  if (boton) boton.classList.add("activo");


  for (var i = 0; i < pedidos.length; i++) {
    var estado = pedidos[i].getAttribute("data-estado");

    if (tipo === "todos" || estado === tipo) {
      pedidos[i].style.display = "flex"; 

      
      var link = pedidos[i].querySelector("h3 a");
      if (link) {    
        link.style.cursor = "pointer";  
      }

    } else {
      pedidos[i].style.display = "none"; 
    }
  }
}


filtrar("todos");