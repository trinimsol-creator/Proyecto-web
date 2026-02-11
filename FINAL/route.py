from flask import app, render_template, request, redirect, url_for
from controller import *

def route(app):
    print(">>> CARGANDO ROUTE.PY <<<")


    @app.route("/")
    def home():
        return home_pagina()
        
    @app.route("/carrito")
    def carrito():
        return carrito_pagina()
    
    @app.route("/catalogo")
    def catalogo():
        return catalogo_pagina()
        
    @app.route("/detalles")
    def detalles():
        return detalles_pagina()
        
        
    ##### INICIO SESION Y REGISTRARSE ######
    
    
    @app.route("/login")
    def login():
        
        param={}
        return login_pagina(param) 
    
    @app.route("/signin", methods =["GET", "POST"])
    def signin():
        if request.method == "GET":
            return signin_pagina()
        else:
            return registrarUsuario(request.form.to_dict())

    @app.route('/iniciar', methods =["GET", "POST"])  #el usuario inicie sesion 
    def iniciar(): 
        
        param={}
        return ingresoUsuarioValido(param,request)

    @app.route("/logout", endpoint="logout")
    def logout_route():
        cerrarSesion()
        return redirect('/')

    @app.route("/miscompras")
    def miscompras():
        return miscompras_pagina()
        
    @app.route("/pago", methods =["GET", "POST"])
    def pago():
        return pago_pagina()
        
        #parte admin, solo rutas:

    @app.route("/admin")
    def admin():
        return admin_pagina()

    @app.route("/lista-pedidos")
    def lista_pedidos():
        return lista_pedidos_pagina()

    @app.route("/detalle-pedido/<int:id>", methods=["GET", "POST"])
    def detalle_pedido(id):
        return detalle_pedido_pagina(id, request)

    @app.route("/editar_producto/<int:id>", methods=["GET", "POST"])
    def editar_producto(id):
        return editar_producto_pagina(id, request)

    @app.route("/crear-producto", methods=["GET", "POST"])
    def crear_producto():
        return crear_producto_pagina(request)

    @app.route("/login-admin", methods=["GET", "POST"])
    def login_admin():
        return login_admin_pagina(request)
        
    @app.route("/logout-admin")
    def logout_admin_route():
         return logout_admin()
        
    @app.route("/ajax/actualizar_carrito", methods=["POST"])
    def ajax_actualizar_carrito():
        id = request.form.get("id")
        cantidad = int(request.form.get("cantidad"))

        actualizar_cantidad_carrito(id, cantidad)

        carrito = obtener_carrito()
        total, total_transferencia = calcular_total(carrito)

        html = f"""
        <h2>Total: ${total}</h2>
        <p class="discount-total">
        Total con descuento por transferencia bancaria: ${total_transferencia}
        </p>
        """

        return html





    @app.route("/ajax/eliminar_producto", methods=["POST"])
    def ajax_eliminar_producto():
        id = request.form.get("id")

        eliminar_producto_carrito(id)

        carrito = obtener_carrito()
        total, total_transferencia = calcular_total(carrito)

        html = f"""
        <h2>Total: ${total}</h2>
        <p class="discount-total">
            Total con descuento por transferencia bancaria: ${total_transferencia}
        </p>
        """

        return html



    @app.route("/ajax/agregar_carrito", methods=["POST"])
    def ajax_agregar_carrito():
        id = request.form.get("id")
        cantidad = int(request.form.get("cantidad"))

        producto = obtenerProductoPorId(id)

        agregar_producto_carrito(producto, cantidad)

        return "ok"




#paginas no encontradas

#    @app.route('/<name>')
#    def noEncontrada(name):        
#        return paginaNoEncontrada(name)
  
  
  
