"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    # Inicializar un diccionario para almacenar la suma de la columna 2 por letra de la columna 4
    suma_columna_2 = {}

    # Especificar la ruta completa del archivo
    #ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    # Abrir el archivo y leer línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones y obtener las columnas necesarias
            columnas = linea.split('\t')
            try:
                # Obtener la columna 2 y 4
                columna_2 = int(columnas[1])
                columna_4 = columnas[3]
                # Dividir la columna 4 por comas
                letras = columna_4.split(',')
                for letra in letras:
                    # Sumar el valor de la columna 2 a la letra correspondiente en el diccionario
                    if letra in suma_columna_2:
                        suma_columna_2[letra] += columna_2
                    else:
                        suma_columna_2[letra] = columna_2
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue

    # Ordenar el diccionario alfabéticamente y devolverlo
    resultado = dict(sorted(suma_columna_2.items()))
    return resultado
print(pregunta_11())