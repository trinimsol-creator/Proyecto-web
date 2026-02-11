from _mysql_db import *

from appConfig import config

BASE = config['db']

def obtenerPedidos():
    sql = """
        SELECT 
            compras.id,
            compras.fechahora,
            compras.total,
            compras.estado,
            usuario.nombre,
            usuario.apellido
        FROM compras
        INNER JOIN usuario ON compras.id_usuario = usuario.id
        ORDER BY compras.fechahora DESC
    """
    return selectDB(BASE, sql, dictionary=True)

# ---------------- PRODUCTOS ----------------
#pprin admin
def obtenerProductosAdmin():
    sql = """
        SELECT id, nombre, img
        FROM producto
        ORDER BY id DESC
    """
    return selectDB(BASE, sql, dictionary=True)
def actualizarProducto(id, datos):
    sql = """
        UPDATE producto
        SET nombre=%s,
            precio=%s,
            detalles=%s,
            categoria=%s,
            color=%s,
            stock=%s,
            estado=%s,
            img=%s
        WHERE id=%s
    """
    valores = (
        datos["nombre"],
        datos["precio"],
        datos["detalles"],
        datos["categoria"],
        datos["color"],
        datos["stock"],
        datos["estado"],
        datos["img"],
        id
    )
    return updateDB(BASE, sql, valores)

def obtenerProductoPorId(id_prod):
    sSql = """
        SELECT id, nombre, precio, detalles, categoria, estado, color, img
        FROM producto
        WHERE id = %s
    """
    filas = selectDB(BASE, sSql, (id_prod,))

    if filas:
        f = filas[0]
        return {
            "id": f[0],
            "nombre": f[1],
            "precio": f[2],
            "detalles": f[3],
            "categoria": f[4],
            "estado": f[5],
            "color": f[6],
            "img": f[7]
        }
    return None

#detalles del pedidp
def obtenerPedidoPorId(id_pedido):
    sql = """
        SELECT 
            compras.id,
            compras.fechahora,
            compras.total,
            compras.estado,
            usuario.nombre,
            usuario.apellido
        FROM compras
        INNER JOIN usuario ON compras.id_usuario = usuario.id
        WHERE compras.id = %s
    """
    filas = selectDB(BASE, sql, (id_pedido,), dictionary=True)
    return filas[0] if filas else None

def obtenerProductosPorPedido(id_pedido):
    sql = """
        SELECT 
            producto.nombre,
            detalles_compras.cantidad,
            detalles_compras.precio_unidad
        FROM detalles_compras
        INNER JOIN producto ON detalles_compras.id_producto = producto.id
        WHERE detalles_compras.id_compra = %s
    """
    return selectDB(BASE, sql, (id_pedido,), dictionary=True)

def actualizarEstadoPedido(id_pedido, nuevo_estado):
    sql = """
        UPDATE compras
        SET estado = %s
        WHERE id = %s
    """
    return updateDB(BASE, sql, (nuevo_estado, id_pedido))


def crearProducto(datos):
    sQuery = """
        INSERT INTO producto
        (nombre, precio, detalles, categoria, color, img)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    val = (
        datos['nombre'],
        datos['precio'],
        datos['detalles'],
        datos['categoria'],
        datos['color'],
        datos['img']
    )
    return insertDB(BASE, sQuery, val)
#catalogo
def obtenerProductosCatalogo():
    sql = """
        SELECT id, nombre, precio, img
        FROM producto
        WHERE estado = 'visible'
    """
    return selectDB(BASE, sql, dictionary=True)


#para miscompras
def obtenerComprasUsuario(id_usuario):
    sql = """
        SELECT 
            c.id,
            c.fechahora,
            c.total,
            c.estado,
            p.id AS id_producto,
            p.nombre,
            p.img
        FROM compras c
        INNER JOIN detalles_compras dc ON c.id = dc.id_compra
        INNER JOIN producto p ON dc.id_producto = p.id
        WHERE c.id_usuario = %s
        ORDER BY c.fechahora DESC
    """
    return selectDB(BASE, sql, (id_usuario,), dictionary=True)



# ---------------- USUARIOS ----------------

def obtenerUsuarioLogin(email, password):
    sSql = """
        SELECT id, nombre, email
        FROM usuario
        WHERE email=%s AND pass=%s
    """
    filas = selectDB(BASE, sSql, (email, password))

    if filas:
        f = filas[0]
        return {
            "id": f[0],
            "nombre": f[1],
            "email": f[2]
        }
    return None

# LOGIN Y SIGNIN



def crearUsuario(di):
    sQuery = """
        INSERT INTO usuario
        (nombre_usuario, email, pass, nombre, apellido, tipo_usario, dni, direccion)
        VALUES (%s,%s,%s,%s,%s,'cliente',%s,%s)
    """
    val = (
        di.get('username'),
        di.get('email'),
        di.get('password'),
        di.get('nombre'),
        di.get('apellido'),
        di.get('dni'),
        di.get('direccion')
    )

    return insertDB(BASE, sQuery, val) == 1



def obtenerUsuarioXEmail(param,email,clave='usuario'):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'.
       Carga la información obtenida de la BD en el dict 'param'
       Recibe 'param' in diccionario
       Recibe 'email' que es el mail si se utiliza como clave en la búsqueda
       Recibe 'clave' que es a clave que se le colocará al dict 'param'
       
    '''
    sSql="""SELECT id, nombre,apellido,email,pass 
    FROM  usuario WHERE  email=%s;""" 
    val=(email,)

    fila=selectDB(BASE,sSql,val)
    param[clave]={}
    param[clave]['id']=fila[0][0]
    param[clave]['nombre']=fila[0][1]
    param[clave]['apellido']=fila[0][2]
    param[clave]['email']=fila[0][3]
    param[clave]['password']=fila[0][4]





def actualizarUsuario(di,email):
    '''### Información:
        Actualiza el registro de la tabla usuario para la clave 'email'
        Recibe 'di' un dict con los campos que se requiere modificar.
        Recibe 'email' que es la clave para identificar el regsitro a actualizar.
        Retorna True si realiza la actualización correctamente.
                False caso contrario.

    '''
    sQuery="""update usuario 
        SET nombre=%s, 
        apellido=%s,
        pass=%s 
        WHERE email=%s;
        """
    val=(di.get('nombre'), 
         di.get('apellido'), 
         di.get('password'), 
         email )
    
    resul_update=updateDB(BASE,sQuery,val=val)
    return resul_update==1

#log in admin
def obtenerAdminLogin(email, password):
    sql = """
        SELECT id, nombre, apellido, email
        FROM usuario
        WHERE email = %s 
          AND pass = %s 
          AND tipo_usario = 'admin'
    """
    filas = selectDB(BASE, sql, (email, password), dictionary=True)
    return filas[0] if filas else None



########## INICIO DE SESION + REGISTRARSE #####################
def crearUsuario(di, es_admin=False):
    sQuery=""" 
        INSERT INTO usuario
        (nombre_usuario, email, pass, nombre, apellido, tipo_usario, dni, direccion)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    val = (
        di.get('nombre_usuario'),
        di.get('email'),
        di.get('password'),
        di.get('nombre'),
        di.get('apellido'),
        'admin' if es_admin else 'cliente',
        di.get('dni'),
        di.get('direccion')
    )
    resultados_insertar=insertDB(BASE,sQuery,val)
    return resultados_insertar==1


def obtenerUsuarioXEmailPass(result,email,password):
    
    res=False
    sSql="""SELECT id, nombre,apellido,email,pass,tipo_usario 
    FROM  usuario WHERE  email=%s and pass=%s;"""
    val=(email,password)
    fila=selectDB(BASE,sSql,val)

    if fila!=[]:
        res=True
        result['id']=fila[0][0]
        result['nombre']=fila[0][1]
        result['apellido']=fila[0][2]
        result['username']=fila[0][3] # es el mail
        result['password']=fila[0][4]
        result['imagen']=''
        result['tipo_usuario']=fila[0][5]
    return res    