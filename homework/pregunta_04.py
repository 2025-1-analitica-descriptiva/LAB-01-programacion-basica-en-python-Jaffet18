"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

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
                fecha = columnas[2]
                # Obtener el mes de la fecha
                mes = fecha.split('-')[1]
                # Contar la letra en el diccionario
                if mes in conteo_letras:
                    conteo_letras[mes] += 1
                else:
                    conteo_letras[mes] = 1
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(conteo_letras.items())
    return resultado
print(pregunta_04())