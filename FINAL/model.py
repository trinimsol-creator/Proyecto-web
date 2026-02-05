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
    '''### Información:
        Agrega un nuevo usuario (un registro) en la tabla usuario de la DB
        Recibe 'di' un diccionario con los datos del usuario a agegar en la tabla.
        Retorna True si realiza con existo el insert, False caso contrario.
    '''
    sQuery=""" 
        INSERT INTO usuario
        (id, nombre, apellido, email, pass)
        VALUES
        (%s,%s, %s, %s, %s);
    """
    val=(None,di.get('nombre'), di.get('apellido'), di.get('email'), di.get('password'))
    resul_insert=insertDB(BASE,sQuery,val)
    return resul_insert==1


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


def obtenerUsuarioXEmailPass(result,email,password):
    res=False
    sSql="""SELECT id, nombre,apellido,email,pass 
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
        result['rol']=''
    return res    


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