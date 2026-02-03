import mysql.connector

def conectarBD(configDB=None):
    ''' Establece conexión con el servidor MySQL usando el dict de appConfig '''
    mydb = None
    if configDB is not None:
        try:
            mydb = mysql.connector.connect(
                host=configDB.get("host"),
                user=configDB.get("user"),
                password=configDB.get("pass"),
                database=configDB.get("dbname")
            )
        except mysql.connector.Error as e:
            print(f"ERROR DE CONEXIÓN -> {e}")
    return mydb

def cerrarBD(mydb):
    ''' Cierra la conexión activa '''
    if mydb is not None:
        mydb.close()

def consultarDB(mydb, sQuery="", val=None, title=False, dictionary=False):
    ''' Realiza consultas tipo SELECT '''
    myresult = None
    try:
        if mydb is not None:
            mycursor = mydb.cursor()
            if val is None:
                mycursor.execute(sQuery)
            else:
                mycursor.execute(sQuery, val)

            myresult = mycursor.fetchall()

            if title:
                myresult.insert(0, mycursor.column_names)

            if dictionary:
                keys = mycursor.column_names
                myresult = [dict(zip(keys, row)) for row in myresult]
    except mysql.connector.Error as e:
        print(f"ERROR EN SELECT -> {e}")
    return myresult

def ejecutarDB(mydb, sQuery="", val=None):
    ''' Realiza consultas tipo INSERT, UPDATE, DELETE '''
    res = None
    try:
        mycursor = mydb.cursor()
        if val is None:
            mycursor.execute(sQuery)
        else:
            mycursor.execute(sQuery, val)
        mydb.commit()
        res = mycursor.rowcount
    except mysql.connector.Error as e:
        mydb.rollback()
        print(f"ERROR EN EJECUCIÓN -> {e}")
    return res

#####FUNCIONES SECUNDARIAS#####
def selectDB(configDB=None,sql="",val=None,title=False,dictionary=False):
    resQuery=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        resQuery=consultarDB(mydb,sQuery=sql,val=val,title=title,dictionary=dictionary)
        cerrarBD(mydb)
    return resQuery

def insertDB(configDB=None,sql="",val=None):
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

def updateDB(configDB=None,sql="",val=None):
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

def deleteDB(configDB=None,sql="",val=None):
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res




from appConfig import config

BASE = config['db']