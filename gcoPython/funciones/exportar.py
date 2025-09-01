import os
from openpyxl import Workbook
from db.conexion import obtener_conexion
from datetime import datetime


def exportar_clientes():
    """
    Exporta todos los clientes a un archivo Excel dentro de la carpeta 'export/excel'.
    El archivo incluye un timestamp en el nombre para diferenciar cada exportación.
    """
    conexion = obtener_conexion()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

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

    if not resultados:
        print("No hay clientes para exportar.")
        return

    # Crear carpeta export/excel si no existe
    carpeta = "export/excel"
    os.makedirs(carpeta, exist_ok=True)

    # Nombre dinámico con fecha y hora
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(carpeta, f"clientes_{fecha}.xlsx")

    # Crear archivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Clientes"

    # Escribir encabezados
    encabezados = resultados[0].keys()
    ws.append(list(encabezados))

    # Escribir filas de datos
    for cliente in resultados:
        ws.append(list(cliente.values()))

    wb.save(ruta)
    print(f"Archivo '{ruta}' exportado correctamente con {len(resultados)} clientes.")
