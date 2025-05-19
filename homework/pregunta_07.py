"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    # Inicializar un diccionario para contar la cantidad de registros por letra
    conteo_letras = {}

    # Especificar la ruta completa del archivo
    #ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    # Abrir el archivo y leer línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones y obtener la primera columna (índice 0)
            columnas = linea.split('\t')
            try:
                # Obtener la columna 2 y 1
                columna_2 = columnas[1]
                columna_1 = columnas[0]
                # Convertir la columna 2 a entero
                columna_2 = int(columna_2)
                # Contar la letra en el diccionario
                if columna_2 in conteo_letras:
                    conteo_letras[columna_2].append(columna_1)
                else:
                    conteo_letras[columna_2] = [columna_1]
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(conteo_letras.items())
    return resultado
print(pregunta_07())