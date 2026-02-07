
from flask import render_template, request, redirect, url_for, session
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config

def home_pagina():
    param = {}
    return render_template("PPrincipal.html", param=param)

#funciones para admin


def admin_pagina():
    productos = obtenerProductosAdmin()
    return render_template("PPrin_admin.html", productos=productos)


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
    
    print("REQUEST METHOD:", request.method)
    print("FORM DATA:", request.form)
    print("FILES:", request.files)

    producto = obtenerProductoPorId(id)

    if not producto:
        return "Producto no encontrado", 404

    if request.method == "POST":

        nombre    = request.form.get("nombre")
        precio    = request.form.get("precio")
        detalles  = request.form.get("detalles")
        categoria = request.form.get("categoria")
        estado    = request.form.get("estado")
        color     = request.form.get("color")
        stock     = request.form.get("stock")

        img_actual = producto["img"]
        foto = request.files.get("archivo")

        if foto and foto.filename != "":
            filename = secure_filename(foto.filename)
            ext = filename.rsplit(".", 1)[1]
            nombre_img = f"{uuid4()}.{ext}"

            ruta = os.path.join(config['upload_folder'], nombre_img)
            foto.save(ruta)
        else:
            nombre_img = img_actual

        datos = {
            "nombre": nombre,
            "precio": precio,
            "detalles": detalles,
            "categoria": categoria,
            "estado": estado,
            "color": color,
            "stock": stock,
            "img": nombre_img
        }

        actualizarProducto(id, datos)

        return redirect(url_for("admin"))

    return render_template("Editar_Prod.html", producto=producto)


def crear_producto_pagina(request):
    print("ENTRÓ A crear_producto_pagina")
    print("METHOD:", request.method)

    if request.method == "POST":

        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        detalles = request.form.get("detalles")
        categoria = request.form.get("categoria")
        color = request.form.get("color")

        foto = request.files.get("archivo")

        nombre_img = None

        if foto and foto.filename != "":
            filename = secure_filename(foto.filename)
            ext = filename.rsplit(".",1)[1]
            nombre_img = f"{uuid4()}.{ext}"

            ruta = os.path.join(config['upload_folder'], nombre_img)
            foto.save(ruta)

        datos = {
            "nombre": nombre,
            "precio": precio,
            "detalles": detalles,
            "categoria": categoria,
            "color": color,
            "img": nombre_img
        }

        print("INSERTANDO PRODUCTO:", datos)

        crearProducto(datos)

        return redirect(url_for("admin"))

    return render_template("Crear_Prod.html")


#log in admin
def login_admin_pagina(request):
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        admin = obtenerAdminLogin(email, password)

        if admin:
            session["admin"] = True
            session["admin_nombre"] = admin["nombre"]
            return redirect(url_for("admin"))
        else:
            return render_template(
                "Login_Admin.html",
                error="Credenciales incorrectas"
            )

    return render_template("Login_Admin.html")
#log out admin
def logout_admin():
    session.pop("admin", None)
    session.pop("admin_nombre", None)
    return redirect(url_for("login_admin"))



# ================= pantallas vicky=================

def carrito_pagina():
    param = {}
    return render_template("carrito.html", param=param)

def catalogo_pagina():
    productos = obtenerProductosCatalogo()
    return render_template("Catalogo.html", productos=productos)


def detalles_pagina():
    param = {}
    return render_template("detalles.html", param=param)

def login_pagina(param):
    return render_template("Login.html", param=param)

def signin_pagina(param):
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



#FUNCIONES PARA LOGIN Y SIGNIN

def getRequet(request):
    try: 
        if request.method =="POST":                           # Solicitud x POST, creación de una session
            myrequest=request.form          
        elif request.method =="GET" and len(request.args)!=0: # Solicitud x GET, creación de una session
            myrequest=request.args
        else:
            myrequest={}
    except ValueError:                              
        myrequest={}
    return myrequest


def cargarSesion(dicUsuario):
    session['id_usuario'] = dicUsuario['id']
    session['nombre']     = dicUsuario['nombre']
    session['apellido']   = dicUsuario['apellido']
    session['username']   = dicUsuario['username'] # es el mail
    session['imagen']     = ""
    session['rol']        = ""
    session["time"]       = datetime.now()  

def crearSesion(request):

    sesionValida=False
    mirequest={}
    try: 
        #Carga los datos recibidos del form cliente en el dict 'mirequest'.          
        getRequet(mirequest)
        # CONSULTA A LA BASE DE DATOS. Si usuario es valido => crea session
        dicUsuario={}
        if obtenerUsuarioXEmailPass(dicUsuario,mirequest.get("username"),mirequest.get("password")):
            # Carga sesion (Usuario validado)
            cargarSesion(dicUsuario)
            sesionValida = True
    except ValueError:                              
        pass
    return sesionValida

def haySesion():  
    return session.get("username")!=None

def cerrarSesion():
    try:    
        session.clear()
    except:
        pass
    
    
#LOGIN Y SINGIN

def ingresoUsuarioValido(param,request):
    if crearSesion(request):
        return redirect(url_for("home"))
    else:
        param['error_msg_login']="Error: Usuario y/o password inválidos"
        return login_pagina(param)        


def registro_pagina(param):   
    return render_template('register.html',param=param)

def ValidarFormularioRegistro(di):
    res=True
    res= res and di.get('nombre')!=""
    res= res and di.get('apellido')!=""
    res= res and di.get('email')!=""
    res= res and di.get('password')!=""
    return res

def registrarUsuario(param,request):
    mirequest={}
    getRequet(mirequest)
    
    if ValidarFormularioRegistro(mirequest):
        # CONSULTA A LA BASE DE DATOS: Realiza el insert en la tabla usuario
        if crearUsuario(mirequest):
            param['succes_msg_login']="Se ha creado el usuario con exito"
            cerrarSesion()           # Cierra sesion existente(si la hubiere)
            res=login_pagina(param)  # Envia al login para que vuelva a loguearse el usuario
        else:
            param['error_msg_register']="Error: No se ha podido crear el usuario"
            res=registro_pagina(param)
    else:
        param['error_msg_register']="Error: Problema en la validacion de los campos"
        res=registro_pagina(param)

    return res 

def editarUsuario_pagina(param):
    res= redirect('/') # redirigir al home o a la pagina del login

    if haySesion():    # hay session?
        # Confecciona la pagina en cuestion
        obtenerUsuarioXEmail(param,session.get('username'), 'edit_user')
        res= render_template('edit_user.html',param=param)
           
    return res  


def actualizarDatosDeUsuarios(param,request):
    res=False
    msj=""
    mirequest={}
    try:     
        getRequet(mirequest)      
        # *** ACTUALIZAR USUARIO ***
        
        if actualizarUsuario(mirequest,session.get("username")):
            res=True
            param['succes_msg_updateuser']="Se ha ACTUALIZADO el usuario con exito"
        else:
            #error
            res=False
            param['error_msg_updateuser']="Error: No se ha podido ACTUALIZAR el usuario"

        editarUsuario_pagina(param)
        res= render_template('edit_user.html',param=param)  
    except ValueError as e :                   
        pass
    return res 