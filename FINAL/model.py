from _mysql_db import *

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

