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
    dic_suma = {}
    
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            elementos = linea.strip().split('\t')
            clave = elementos[0]
            pares_col5 = elementos[4].split(',')  # Separa por comas
            suma = 0
            # print(pares_col5)
            for par in pares_col5:
                _, valor = par.split(':')  # Extrae el valor después de ':'
                suma += int(valor)
                #print(clave, suma)
            dic_suma[clave] = dic_suma.get(clave, 0) + suma
    # Ordenar el diccionario por clave
    return dict(sorted(dic_suma.items()))

print(pregunta_12())