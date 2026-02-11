function queryAjax(url, idDest, method = "POST", dataSend = null) {

    const xhr = new XMLHttpRequest();     

    if (xhr) {
        xhr.timeout = 2000;
        xhr.open(method, url, true);
        document.body.style.cursor = 'wait';

        xhr.onload = function () {
            document.body.style.cursor = 'default';

            if (xhr.status === 200) {
                if (idDest) {
                    setDataIntoNode(idDest, xhr.responseText);
                }
            } else {
                console.error("Error AJAX:", xhr.status, xhr.responseText);
                alert("Ocurrió un error al comunicarse con el servidor.");
            }
        };

        xhr.ontimeout = function () {
            console.log("Terminado por expiración de tiempo");
        };

        xhr.onloadend = function () {
            document.body.style.cursor = 'default';
        };

        xhr.send(dataSend);
    }
    else {
        console.log('No se pudo instanciar el objeto AJAX!');
    }
}

function setDataIntoNode(idDest, textHTML) {

    var oElement;
    var sNameTag;
    var elementsReadOnlyInnerHTML;

    elementsReadOnlyInnerHTML = [
        "INPUT","COL","COLGROUP","FRAMESET","HEAD","HTML",
        "STYLE","TABLE","TBODY","TFOOT","THEAD","TITLE","TR"
    ];

    if (document.getElementById(idDest)) {
        oElement = document.getElementById(idDest);
        sNameTag = oElement.tagName.toUpperCase();

        if (elementsReadOnlyInnerHTML.indexOf(sNameTag) === -1) {
            oElement.innerHTML = textHTML;
        }
        else if (sNameTag === 'INPUT') {
            oElement.value = textHTML;
        }
        else {
            setAnyInnerHTML(oElement, textHTML);
        }
    }
    else {
        console.log('El elemento destino cuyo id="' + idDest + '" no existe!');
    }
}

function setAnyInnerHTML(oElement, html) {
    var temp = oElement.ownerDocument.createElement('div');
    temp.innerHTML = html;
    oElement.parentNode.replaceChild(temp.firstChild.firstChild, oElement);
}

document.addEventListener("DOMContentLoaded", function () {

    var inputs = document.querySelectorAll(".cantidad");
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener("change", cambiarCantidad);
    }

    var botones = document.querySelectorAll(".remove-btn");
    for (var j = 0; j < botones.length; j++) {
        botones[j].addEventListener("click", eliminarProducto);
    }

});

function cambiarCantidad(e) {
    var card = e.target.closest(".product-card");
    var idProducto = card.dataset.id;
    var cantidad = e.target.value;

    var data = new FormData();
    data.append("id", idProducto);
    data.append("cantidad", cantidad);

    queryAjax("/ajax/actualizar_carrito", "total-carrito", "POST", data);
}
function eliminarProducto(e) {
    var card = e.target.closest(".product-card");
    var idProducto = card.dataset.id;

    var data = new FormData();
    data.append("id", idProducto);

    queryAjax("/ajax/eliminar_producto", "total-carrito", "POST", data);

    card.remove();
}
function agregarCarrito(idProducto) {
    var cantidad = document.getElementById("cantidad").value;

    var data = new FormData();
    data.append("id", idProducto);
    data.append("cantidad", cantidad);

    queryAjax("/ajax/agregar_carrito", "", "POST", data);

    mostrarToast("Producto agregado al carrito");
}

function mostrarToast(texto) {
    var toast = document.createElement("div");
    toast.className = "toast-msg";
    toast.innerText = texto;

    document.body.appendChild(toast);

    setTimeout(function () {
        toast.classList.add("show");
    }, 10);

    setTimeout(function () {
        toast.classList.remove("show");
        setTimeout(function () {
            toast.remove();
        }, 300);
    }, 2500);
}
