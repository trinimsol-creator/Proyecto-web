from flask import render_template, request, redirect, url_for
from model import *

def home_pagina():
    param = {}
    return render_template("PPrincipal.html", param=param)

#funciones para admin

def admin_pagina():
    param = {}
    return render_template("PPrin_admin.html", param=param)

def lista_pedidos_pagina():
    pedidos = obtenerPedidos()
    return render_template("Lista_pedidos.html", pedidos=pedidos)


def detalle_pedido_pagina(id, request):

    if request.method == "POST":
        nuevo_estado = request.form.get("estado")
        actualizarEstadoPedido(id, nuevo_estado)

    pedido_db = obtenerPedidoPorId(id)
    productos = obtenerProductosPorPedido(id)

    if not pedido_db:
        return "Pedido no encontrado", 404

    pedido = {
        "id": pedido_db["id"],
        "cliente": f'{pedido_db["nombre"]} {pedido_db["apellido"]}',
        "fecha": pedido_db["fechahora"],
        "total": pedido_db["total"],
        "estado": pedido_db["estado"],
        "productos": productos
    }

    return render_template("Detalle_del_Pedido.html", pedido=pedido)

def editar_producto_pagina(id, request):
    producto_datos = {
        "id": id,
        "nombre": "Top Ariel",
        "precio": 25000,
        "detalles": "Top de color negro",
        "categoria": "Top",
        "estado": "Stock",
        "color": "n",
        "imagen": "top_ariel.jpg"
    }

    if request.method == "POST":
        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        detalles = request.form.get("detalles")
        categoria = request.form.get("categoria")
        estado = request.form.get("estado")
        color = request.form.get("color")

        foto = request.files.get("archivo")
        if foto and foto.filename != "":
            print(f"Nueva foto recibida: {foto.filename}")

        print(f"Producto {id} actualizado: {nombre}, ${precio}")
        return redirect(url_for("admin"))

    return render_template("Editar_Prod.html", producto=producto_datos)


def crear_producto_pagina(request):
    if request.method == "POST":
        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        detalles = request.form.get("detalles")
        categoria = request.form.get("categoria")
        color = request.form.get("color")

        foto = request.files.get("archivo")

        print("--- NUEVO PRODUCTO RECIBIDO ---")
        print(f"Nombre: {nombre}")
        print(f"Precio: {precio}")
        print(f"Categoría: {categoria}")
        print(f"Color: {color}")

        if foto and foto.filename != "":
            print(f"Imagen: {foto.filename}")

        return redirect(url_for("admin"))

    return render_template("Crear_Prod.html")


def login_admin_pagina(request):
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@coast.com" and password == "1234":
            print(f"Login exitoso: {email}")
            return redirect(url_for("lista_pedidos"))
        else:
            return render_template(
                "Login_Admin.html",
                error="Credenciales incorrectas"
            )

    return render_template("Login_Admin.html")


# ================= pantallas vicky=================

def carrito_pagina():
    param = {}
    return render_template("carrito.html", param=param)

def catalogo_pagina():
    param = {}
    return render_template("Catalogo.html", param=param)

def detalles_pagina():
    param = {}
    return render_template("detalles.html", param=param)

def login_pagina():
    param = {}
    return render_template("Login.html", param=param)

def signin_pagina(request):
    param = {}
    return render_template("Signin.html", param=param)

def miscompras_pagina():
    param = {}
    return render_template("miscompras.html", param=param)

def pago_pagina():
    param = {}
    return render_template("pago.html", param=param)


#pagina no encontrada

def paginaNoEncontrada(name):
    res='Pagina "{}" no encontrada<br>'.format(name)
    res+='<a href="{}">{}</a>'.format("/","Home")
    
    return res
