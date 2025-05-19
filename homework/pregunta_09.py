"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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
                # Obtener la columna 5
                columna_5 = columnas[4]
                # Dividir la columna 5 por comas
                pares = columna_5.split(',')
                for par in pares:
                    # Dividir cada par por `:`
                    clave, valor = par.split(':')
                    # Contar la letra en el diccionario
                    if clave in conteo_letras:
                        conteo_letras[clave] += 1
                    else:
                        conteo_letras[clave] = 1
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Devolver el diccionario con los conteos
    resultado = sorted(conteo_letras.items())
    return resultado
print(pregunta_09())