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

