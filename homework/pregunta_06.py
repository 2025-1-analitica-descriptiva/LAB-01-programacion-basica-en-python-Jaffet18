"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
                    # Convertir el valor a entero
                    valor = int(valor)
                    # Contar la letra en el diccionario
                    if clave in conteo_letras:
                        conteo_letras[clave].append(valor)
                    else:
                        conteo_letras[clave] = [valor]
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Inicializar una lista para almacenar los resultados
    resultado = []
    # Recorrer el diccionario y calcular el maximo y minimo por letra

    for letra, valores in conteo_letras.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((letra, minimo, maximo))
    # Ordenar la lista de resultados alfabéticamente por letra
    resultado.sort(key=lambda x: x[0])
    return resultado
print(pregunta_06())