"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 que corresponden a esa clave,
    ordenadas alfabeticamente. Para ello se deben extraer los valores que numéricos
    de la columna 5, que se encuentran separados por comas. El resultado
    debe ser un diccionario con la siguiente estructura:

    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    # Se crea el diccionario vacío para almacenar las sumas
    dic_suma = {}
    #ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    with open('files/input/data.csv', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            elementos = linea.strip().split('\t')
            clave = elementos[0]
            valores_col5 = elementos[4]

            # Extraer solo los dígitos y sumarlos con un comprenhension
            suma = sum(int(c) for c in valores_col5 if c.isdigit())

            # Se ctualiza el diccionario con las sumas
            if clave in dic_suma:
                dic_suma[clave] += suma
            else:
                dic_suma[clave] = suma

    return dict(sorted(dic_suma.items()))

print(pregunta_12())