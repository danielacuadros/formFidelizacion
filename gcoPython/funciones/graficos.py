import os
import matplotlib.pyplot as plt
from db.conexion import obtener_conexion
from datetime import datetime

def clientes_por_ciudad():
    """Genera un gráfico de barras con la cantidad de clientes por ciudad y lo guarda como imagen."""
    conexion = obtener_conexion()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()
    cursor.execute("""
        SELECT ci.nombre_ciudad, COUNT(*) 
        FROM cliente c
        JOIN ciudades ci ON c.id_ciudad = ci.id_ciudad
        GROUP BY ci.nombre_ciudad
    """)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    if not resultados:
        print("No hay datos para graficar.")
        return

    ciudades, cantidades = zip(*resultados)

    plt.figure(figsize=(8,5))
    plt.bar(ciudades, cantidades)
    plt.title("Clientes por Ciudad")
    plt.xlabel("Ciudad")
    plt.ylabel("Cantidad")

    # Crear carpeta export/graficos si no existe
    carpeta = "export/graficos"
    os.makedirs(carpeta, exist_ok=True)

    # Nombre dinámico del archivo con fecha y hora
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(carpeta, f"clientes_por_ciudad_{fecha}.png")
    plt.savefig(ruta)
    plt.close()

    print(f"Gráfico guardado en {ruta}")


def clientes_por_marca():
    """Genera un gráfico circular con la distribución de clientes por marca y lo guarda como imagen."""
    conexion = obtener_conexion()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()
    cursor.execute("""
        SELECT m.nombre_marca, COUNT(*) 
        FROM cliente c
        JOIN marcas m ON c.id_marca = m.id_marca
        GROUP BY m.nombre_marca
    """)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    if not resultados:
        print("No hay datos para graficar.")
        return

    marcas, cantidades = zip(*resultados)

    plt.figure(figsize=(8,5))
    plt.pie(cantidades, labels=marcas, autopct="%1.1f%%", startangle=90)
    plt.title("Clientes por Marca")

    carpeta = "export/graficos"
    os.makedirs(carpeta, exist_ok=True)

    # Nombre dinámico del archivo con fecha y hora
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(carpeta, f"clientes_por_marca_{fecha}.png")
    plt.savefig(ruta)
    plt.close()

    print(f"Gráfico guardado en {ruta}")
