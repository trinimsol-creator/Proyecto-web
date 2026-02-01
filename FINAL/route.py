from flask import app, render_template, request, redirect, url_for
from controller import *

def route(app):

        @app.route("/")
        def home():
            return render_template("PPrincipal.html")
            
        @app.route("/carrito")
        def carrito():
            '''
            Info:
            Carga la página del carrito.
            Por ahora solo renderiza la vista.
            Luego se conectará con controller y model.
            '''
            param = {}
            return render_template("carrito.html", param=param)
        
        
        @app.route("/catalogo")
        def catalogo():
            '''
            Info:
            Carga la página del catalogo.
            Por ahora solo renderiza la vista.
            Luego se conectará con controller y model.
            '''
            param = {}
            return render_template("Catalogo.html", param=param)
        
        @app.route("/detalles")
        def detalles():

            param = {}
            return render_template("detalles.html", param=param)
        
        @app.route("/login")
        def login():
            ''' Info:
            Carga la pagina del login  
            ''' 
            param={}
            return render_template("Login.html", param=param)
        
        @app.route('/signin', methods =["GET", "POST"])
        def signin(): 
            ''' Info: 
            Recepciona la solicitud request que es enviada
            desde el formulario de login 
            retorna la pagina home en caso de exito 
                    o la pagina login en caso de fracaso
            '''
            param={}
            return render_template("Signin.html", param=param)

        @app.route("/miscompras")
        def miscompras():
            ''' Info:
            Carga la pagina de mis comrpas  
            ''' 
            param={}
            return render_template("miscompras.html", param=param)
        
        @app.route("/pago")
        def pago():
            ''' Info:
            Carga la pagina de mis comrpas  
            ''' 
            param={}
            return render_template("pago.html", param=param)
        
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

        @app.route("/editar-producto/<int:id>", methods=["GET", "POST"])
        def editar_producto(id):
            return editar_producto_pagina(id, request)

        @app.route("/crear-producto", methods=["GET", "POST"])
        def crear_producto():
            return crear_producto_pagina(request)

        @app.route("/login-admin", methods=["GET", "POST"])
        def login_admin():
            return login_admin_pagina(request)

  