document.addEventListener("DOMContentLoaded", function() {


  var botonesEliminar = document.getElementsByClassName("remove-btn");


  for (var i = 0; i < botonesEliminar.length; i++) {
    
   
    botonesEliminar[i].addEventListener("click", function() {
      
      
      var botonPresionado = this;

      
      var tarjetaProducto = botonPresionado.parentElement;

      
      tarjetaProducto.style.display = "none";
    });
  }

});
