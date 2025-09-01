from db.conexion import obtener_conexion

# Buscar por número de identificación
def buscar_por_identificacion(numero_identificacion):
    conexion = obtener_conexion()
    if not conexion:
        return None
    cursor = conexion.cursor(dictionary=True)
    query = """
        SELECT c.id, c.tipo_identificacion, c.numero_identificacion, 
               c.nombres, c.apellidos, c.fecha_nacimiento, c.direccion,
               ciu.nombre_ciudad, m.nombre_marca
        FROM cliente c
        JOIN ciudades ciu ON c.id_ciudad = ciu.id_ciudad
        JOIN marcas m ON c.id_marca = m.id_marca
        WHERE c.numero_identificacion = %s
    """
    cursor.execute(query, (numero_identificacion,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado


# Buscar por nombre o apellido
def buscar_por_nombre(nombre):
    conexion = obtener_conexion()
    if not conexion:
        return []
    cursor = conexion.cursor(dictionary=True)
    query = """
        SELECT c.id, c.tipo_identificacion, c.numero_identificacion, 
               c.nombres, c.apellidos, c.fecha_nacimiento, c.direccion,
               ciu.nombre_ciudad, m.nombre_marca
        FROM cliente c
        JOIN ciudades ciu ON c.id_ciudad = ciu.id_ciudad
        JOIN marcas m ON c.id_marca = m.id_marca
        WHERE c.nombres LIKE %s OR c.apellidos LIKE %s
    """
    cursor.execute(query, (f"%{nombre}%", f"%{nombre}%"))
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados


# Buscar por ciudad
def buscar_por_ciudad(ciudad):
    conexion = obtener_conexion()
    if not conexion:
        return []
    cursor = conexion.cursor(dictionary=True)
    query = """
        SELECT c.id, c.tipo_identificacion, c.numero_identificacion, 
               c.nombres, c.apellidos, c.fecha_nacimiento, c.direccion,
               ciu.nombre_ciudad, m.nombre_marca
        FROM cliente c
        JOIN ciudades ciu ON c.id_ciudad = ciu.id_ciudad
        JOIN marcas m ON c.id_marca = m.id_marca
        WHERE ciu.nombre_ciudad LIKE %s
    """
    cursor.execute(query, (f"%{ciudad}%",))
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados


# Buscar por marca
def buscar_por_marca(marca):
    conexion = obtener_conexion()
    if not conexion:
        return []
    cursor = conexion.cursor(dictionary=True)
    query = """
        SELECT c.id, c.tipo_identificacion, c.numero_identificacion, 
               c.nombres, c.apellidos, c.fecha_nacimiento, c.direccion,
               ciu.nombre_ciudad, m.nombre_marca
        FROM cliente c
        JOIN ciudades ciu ON c.id_ciudad = ciu.id_ciudad
        JOIN marcas m ON c.id_marca = m.id_marca
        WHERE m.nombre_marca LIKE %s
    """
    cursor.execute(query, (f"%{marca}%",))
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados


# Buscar por rango de fechas de nacimiento
def buscar_por_fecha_nacimiento(fecha_inicio, fecha_fin):
    conexion = obtener_conexion()
    if not conexion:
        return []
    cursor = conexion.cursor(dictionary=True)
    query = """
        SELECT c.id, c.tipo_identificacion, c.numero_identificacion, 
               c.nombres, c.apellidos, c.fecha_nacimiento, c.direccion,
               ciu.nombre_ciudad, m.nombre_marca
        FROM cliente c
        JOIN ciudades ciu ON c.id_ciudad = ciu.id_ciudad
        JOIN marcas m ON c.id_marca = m.id_marca
        WHERE c.fecha_nacimiento BETWEEN %s AND %s
    """
    cursor.execute(query, (fecha_inicio, fecha_fin))
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados
