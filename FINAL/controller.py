from flask import render_template, request, redirect, url_for

def home_pagina():
    return render_template("PPrincipal.html")

#funciones admin

def admin_pagina():
    param = {}
    return render_template("PPrin_admin.html", param=param)

def lista_pedidos_pagina():
    return render_template("Lista_pedidos.html")


def detalle_pedido_pagina(id, request):
    pedido_ejemplo = {
        "id": id,
        "cliente": "Juan Pérez",
        "fecha": "2023-10-27",
        "total": 5500,
        "estado": "Pendiente",
        "productos": [
            {"nombre": "Top Ariel", "cantidad": 1, "precio": 25000}
        ]
    }

    if request.method == "POST":
        nuevo_estado = request.form.get("estado")
        print(f"Cambiando el pedido {id} al estado: {nuevo_estado}")
        pedido_ejemplo["estado"] = nuevo_estado

    return render_template("Detalle_del_Pedido.html", pedido=pedido_ejemplo)


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
