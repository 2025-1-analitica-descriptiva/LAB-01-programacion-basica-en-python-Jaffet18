"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    # Inicializar un diccionario para contar la cantidad de registros por letra
    conteo_letras = {}

    # Especificar la ruta completa del archivo
    ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    # Abrir el archivo y leer línea por línea
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones y obtener la primera columna (índice 0)
            columnas = linea.split('\t')
            try:
                letra = columnas[0]
                # Convertir el segundo elemento a entero
                suma = int(columnas[1])
                # Contar la letra en el diccionario
                if letra in conteo_letras:
                    conteo_letras[letra] += suma
                else:
                    conteo_letras[letra] = suma
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(conteo_letras.items())
    return resultado
print(pregunta_03())
