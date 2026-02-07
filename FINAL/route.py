from flask import app, render_template, request, redirect, url_for
from controller import *

def route(app):

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
        

        
        @app.route("/login", methods=["GET","POST"])
        def login():
            param={}
            if request.method == "POST":
                return ingresoUsuarioValido(param, request)
            return login_pagina(param)
        
        @app.route('/signin', methods =["GET", "POST"])
        def signin(): 
            param={}
            if request.method == "POST":
                return ingresoUsuarioValido2(param, request)
            return signin_pagina(param)


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


#paginas no encontradas

        @app.route('/<name>')
        def noEncontrada(name):        
            return paginaNoEncontrada(name)
  
  
  
