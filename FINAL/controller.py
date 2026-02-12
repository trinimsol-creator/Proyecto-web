
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
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not password:
            return render_template("Login_Admin.html", error="Por favor complete todos los campos")

        admin = obtenerAdminLogin(email, password)

        if admin:
            session["admin"] = True
            session["admin_nombre"] = admin["nombre"]
            return redirect(url_for("admin"))
        else:
            return render_template("Login_Admin.html", error="Credenciales incorrectas")

    return render_template("Login_Admin.html", error=None)

#log out admin
def logout_admin():
    session.pop("admin", None)
    session.pop("admin_nombre", None)
    return redirect(url_for("login_admin"))



# ================= pantallas vicky=================

def carrito_pagina():
    carrito = obtener_carrito()
    total, total_transferencia = calcular_total(carrito)

    session['monto_total'] = total
    session['monto_total_transferencia'] = total_transferencia

    return render_template(
        "carrito.html",
        carrito=carrito,
        total=total,
        total_transferencia=total_transferencia
    )


def catalogo_pagina():
    productos = obtenerProductosCatalogo()
    return render_template("Catalogo.html", productos=productos)

def detalles_pagina():
    id_prod = request.args.get("id")

    if not id_prod:
        return "Producto no especificado", 400

    producto = obtenerProductoPorId(id_prod)

    if not producto:
        return "Producto no encontrado", 404

    # cálculo del descuento (10%)
    precio = producto["precio"]
    producto["precio_descuento"] = round(precio * 0.9, 2)

    return render_template("detalles.html", producto=producto)


def login_pagina(param):
    return render_template("Login.html", param=param)

def signin_pagina():
    return render_template("Signin.html")

def miscompras_pagina():

    if not session.get("id_usuario"):
        return redirect(url_for("login"))

    id_usuario = session.get("id_usuario")

    compras = obtenerComprasUsuario(id_usuario)

    return render_template("miscompras.html", compras=compras)


def pago_pagina():
    return render_template(
        "pago.html", 
        monto_total = session.get('monto_total'),
        monto_total_transferencia = session.get('monto_total_transferencia'),
        direccion = session.get('direccion')
    )

def realizar_pago(form_pago):
    vaciar_carrito()
    return render_template("fin_compra.html")

#pagina no encontrada

#def paginaNoEncontrada(name):
#    res='Pagina "{}" no encontrada<br>'.format(name)
#    res+='<a href="{}">{}</a>'.format("/","Home")
#    
#    return res



#FUNCIONES PARA LOGIN Y SIGNIN

def getRequet(diResult):
    if request.method=='POST':
        for name in request.form.to_dict().keys():
            li=request.form.getlist(name)
            if len(li)>1:
                diResult[name]=request.form.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""
    elif request.method=='GET':  
        for name in request.args.to_dict().keys():
            li=request.args.getlist(name)
            if len(li)>1:
                diResult[name]=request.args.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""    


def cargarSesion(dicUsuario):
    session['id_usuario'] = dicUsuario['id']
    session['nombre']     = dicUsuario['nombre']
    session['apellido']   = dicUsuario['apellido']
    session['username']   = dicUsuario['username'] # es el mail
    session['direccion']  = dicUsuario['direccion']
    session["time"]       = datetime.now()

def crearSesion(request):
    sesionValida=False
    try: 
        email = request.form.get("email")
        password = request.form.get("password")

        dicUsuario = {}
        if obtenerUsuarioXEmailPass(dicUsuario,email,password):
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
    if request.method == "POST":
        if crearSesion(request):
            return redirect(url_for("home"))
        else:
            param["error"] = "Email o contraseña incorrectos"
            return render_template("Login.html", param=param)
    return redirect(url_for("login"))        


def ingresoUsuarioValido2(param, request):

    username = request.form.get("name")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm = request.form.get("confirm_password")

    if password != confirm:
        param["error_msg_login"] = "Las contraseñas no coinciden"
        return signin_pagina(param)

    datos = {
        "username": username,
        "nombre": username,
        "apellido": apellido,
        "email": email,
        "password": password,
        "dni": 11111111,
        "direccion": "Sin dirección"
    }

    if crearUsuario(datos):
        return redirect(url_for("login"))
    else:
        param["error_msg_login"] = "Error creando usuario"
        return signin_pagina(param)
    
# VALIDACIONES

def registro_pagina(param):   
    return render_template('Signin.html',param=param)

def validar_string_no_vacio(s):
    return s is not None and s != ''

def validar_contrasenia(s):
    return s is not None and len(s) >= 4

def validar_email(s):
    # TODO: mejorar la validacion de mails

    if s is None or s == '':
        return False
    if s.count("@") != 1:
        return False

    return True

def ValidarFormularioRegistro(di):
    try:
        di['dni'] = int(di.get('dni'))
    except ValueError:
        return False

    return \
        validar_string_no_vacio(di.get('nombre_usuario')) \
        and validar_string_no_vacio(di.get('nombre')) \
        and validar_string_no_vacio(di.get('apellido')) \
        and validar_email(di.get('email')) \
        and validar_string_no_vacio(di.get('direccion')) \
        and validar_contrasenia(di.get('password')) \
        and di.get('password') == di.get('confirm_password')

def registrarUsuario(data):
    param = {}

    if ValidarFormularioRegistro(data):
        print('usuario validado')
        # CONSULTA A LA BASE DE DATOS: Realiza el insert en la tabla usuario
        if crearUsuario(data):
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



def obtener_carrito():
    return session.get("carrito", [])


def actualizar_cantidad_carrito(id_producto, cantidad):
    carrito = session.get("carrito", [])

    for p in carrito:
        if str(p["id"]) == str(id_producto):
            p["cantidad"] = cantidad

    session["carrito"] = carrito


def eliminar_producto_carrito(id_producto):
    carrito = session.get("carrito", [])

    carrito = [p for p in carrito if str(p["id"]) != str(id_producto)]

    session["carrito"] = carrito

def vaciar_carrito():
    session["carrito"] = []
    session.pop('monto_total')
    session.pop('monto_total_transferencia')

def calcular_total(carrito):
    total = 0
    total_transferencia = 0

    for p in carrito:
        total += p["precio"] * p["cantidad"]
        total_transferencia += p["precio_transferencia"] * p["cantidad"]

    return round(total, 2), round(total_transferencia, 2)

def agregar_producto_carrito(producto, cantidad):
    carrito = session.get("carrito", [])

    for p in carrito:
        if str(p["id"]) == str(producto["id"]):
            p["cantidad"] += cantidad
            session["carrito"] = carrito
            return

    carrito.append({
        "id": producto["id"],
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "precio_transferencia": round(producto["precio"] * 0.9, 2),
        "img": "img/" + producto["img"],
        "cantidad": cantidad
    })

    session["carrito"] = carrito
