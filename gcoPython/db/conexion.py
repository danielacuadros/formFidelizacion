import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    """
    Establece y retorna la conexión a la base de datos MySQL.

    Returns:
        conexion (mysql.connector.connection_cext.CMySQLConnection):
            Objeto de conexión si la conexión fue exitosa.
        None: Si ocurre un error en la conexión.
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clientes_gco'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    return None
