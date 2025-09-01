import os
import pandas as pd
import matplotlib.pyplot as plt

from queries.listar import listar_todos
from queries.buscar import (
    buscar_por_identificacion,
    buscar_por_nombre,
    buscar_por_ciudad,
    buscar_por_marca,
    buscar_por_fecha_nacimiento
)

from funciones.exportar import exportar_clientes
from funciones.graficos import clientes_por_ciudad, clientes_por_marca


# Columnas estándar
COLUMNAS = [
    "ID", "TipoIdentificacion", "NumeroIdentificacion",
    "Nombres", "Apellidos", "FechaNacimiento",
    "Direccion", "Ciudad", "Marca"
]


def mostrar_clientes(resultados):
    if not resultados:
        print("No se encontraron clientes.")
        return

    for c in resultados:
        print(f"ID: {c['id']} | {c['nombres']} {c['apellidos']} | "
              f"Identificación: {c['tipo_identificacion']} {c['numero_identificacion']} | "
              f"Ciudad: {c['nombre_ciudad']} | Marca: {c['nombre_marca']} | "
              f"Fecha Nacimiento: {c['fecha_nacimiento']} | Dirección: {c['direccion']}")


def exportar_resultados(resultados):
    """Exporta resultados filtrados a Excel"""
    if resultados:
        if not os.path.exists('export'):
            os.makedirs('export')
        df = pd.DataFrame(resultados, columns=COLUMNAS)
        ruta = os.path.join("export", "clientes_filtrados.xlsx")
        df.to_excel(ruta, index=False)
        print(f"Resultados exportados en {ruta}")
    else:
        print("No hay resultados para exportar.")


def generar_graficos(resultados):
    """Genera gráficos de clientes por ciudad y marca"""
    if resultados:
        if not os.path.exists('export'):
            os.makedirs('export')

        df = pd.DataFrame(resultados, columns=COLUMNAS)

        # Gráfico 1: Clientes por ciudad
        plt.figure(figsize=(8, 5))
        df['Ciudad'].value_counts().plot(kind='bar', color='skyblue', title='Clientes por Ciudad')
        plt.xlabel('Ciudad')
        plt.ylabel('Cantidad de Clientes')
        plt.tight_layout()
        ruta_ciudad = os.path.join('export', 'grafico_clientes_por_ciudad.png')
        plt.savefig(ruta_ciudad)
        plt.close()

        # Gráfico 2: Clientes por marca
        plt.figure(figsize=(8, 5))
        df['Marca'].value_counts().plot(kind='bar', color='orange', title='Clientes por Marca')
        plt.xlabel('Marca')
        plt.ylabel('Cantidad de Clientes')
        plt.tight_layout()
        ruta_marca = os.path.join('export', 'grafico_clientes_por_marca.png')
        plt.savefig(ruta_marca)
        plt.close()

        print(f"Gráficos generados en:\n - {ruta_ciudad}\n - {ruta_marca}")
    else:
        print("No hay datos para generar los gráficos.")


def mostrar_menu():
    resultados = []

    while True:
        print("\nMenú Principal")
        print("1. Listar todos los clientes")
        print("2. Buscar por número de identificación")
        print("3. Buscar por nombre o apellido")
        print("4. Buscar por ciudad")
        print("5. Buscar por marca")
        print("6. Buscar por fecha de nacimiento")
        print("7. Exportar resultados a Excel")
        print("8. Generar gráficos de clientes por ciudad y marca")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados = listar_todos()
            mostrar_clientes(resultados)

        elif opcion == "2":
            numero = input("Ingresa el número de identificación: ")
            resultado = buscar_por_identificacion(numero)
            resultados = [resultado] if resultado else []
            mostrar_clientes(resultados)

        elif opcion == "3":
            nombre = input("Ingresa el nombre o apellido: ")
            resultados = buscar_por_nombre(nombre)
            mostrar_clientes(resultados)

        elif opcion == "4":
            ciudad = input("Ingresa la ciudad: ")
            resultados = buscar_por_ciudad(ciudad)
            mostrar_clientes(resultados)

        elif opcion == "5":
            marca = input("Ingresa la marca: ")
            resultados = buscar_por_marca(marca)
            mostrar_clientes(resultados)

        elif opcion == "6":
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
            resultados = buscar_por_fecha_nacimiento(fecha_inicio, fecha_fin)
            mostrar_clientes(resultados)

        elif opcion == "7":
            print("\n1. Exportar todos los clientes")
            print("2. Exportar últimos resultados filtrados")
            subop = input("Selecciona una opción: ")

            if subop == "1":
                exportar_clientes()
            elif subop == "2":
                exportar_resultados(resultados)
            else:
                print("Opción inválida.")

        elif opcion == "8":
            clientes_por_ciudad()
            clientes_por_marca()

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
