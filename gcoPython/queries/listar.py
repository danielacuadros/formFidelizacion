from db.conexion import obtener_conexion

def listar_todos():
    """Lista todos los clientes con sus datos, ciudad y marca."""
    conexion = obtener_conexion()

    if not conexion:
        return []

    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT 
        c.id,
        c.tipo_identificacion,
        c.numero_identificacion,
        c.nombres,
        c.apellidos,
        c.fecha_nacimiento,
        c.direccion,
        ci.nombre_ciudad,
        m.nombre_marca
    FROM cliente c
    JOIN ciudades ci ON c.id_ciudad = ci.id_ciudad
    JOIN marcas m ON c.id_marca = m.id_marca
    ORDER BY c.id;
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()
    return resultados
