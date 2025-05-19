"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas que contengan, por cada tupla, la letra de la
    columna 1 y la cantidad de elementos en cada registro de las columnas 4 y 5 
    los cuales están separados por comas.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Inicializar una lista para almacenar los resultados
    resultado = []

    # Especificar la ruta completa del archivo
    #ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    # Abrir el archivo y leer línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones y obtener la primera columna (índice 0)
            columnas = linea.split('\t')
            try:
                # Obtener la columna 1, 4 y 5
                columna_1 = columnas[0]
                columna_4 = columnas[3]
                columna_5 = columnas[4]
                # Contar la cantidad de elementos en las columnas 4 y 5
                conteo_columna_4 = len(columna_4.split(','))
                conteo_columna_5 = len(columna_5.split(','))
                # Agregar el resultado a la lista
                resultado.append((columna_1, conteo_columna_4, conteo_columna_5))
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue

    return resultado
print(pregunta_10())


