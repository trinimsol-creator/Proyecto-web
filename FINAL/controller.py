
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
    param = {}
    return render_template("PPrin_admin.html", param=param)

def lista_pedidos_pagina():
    pedidos = obtenerPedidos()
    return render_template("Lista_pedidos.html", pedidos=pedidos)



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