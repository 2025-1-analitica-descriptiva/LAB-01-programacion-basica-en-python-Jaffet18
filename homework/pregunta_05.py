"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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
                letra = columnas[0]
                # Convertir el segundo elemento a entero
                suma = int(columnas[1])
                # Contar la letra en el diccionario
                if letra in conteo_letras:
                    conteo_letras[letra].append(suma)
                else:
                    conteo_letras[letra] = [suma]
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Inicializar una lista para almacenar los resultados
    resultado = []
    # Recorrer el diccionario y calcular el maximo y minimo por letra
    for letra, valores in conteo_letras.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((letra, maximo, minimo))
    # Ordenar la lista de resultados alfabéticamente por letra
    resultado.sort(key=lambda x: x[0])
    return resultado
print(pregunta_05())