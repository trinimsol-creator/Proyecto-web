    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}    
        slides[slideIndex-1].style.display = "block";  
        setTimeout(showSlides, 5000); 
    }


    //para el boton del carrito "finalizar compra"
document.getElementById("finalizar").addEventListener("click", function() {
    window.location.href = "file:///C:/Users/lenovo/Documents/GitHub/Proyecto-web/carrito/carrito2.html"; // cambiá por la página a la que querés ir
});

