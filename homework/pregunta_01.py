"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    # Inicializar una lista vacía para almacenar los elementos de la segunda columna
    elementos_columna_dos = []

    # Especificar la ruta completa del archivo
    ruta_archivo = r'D:\GitHub\LABORATORIOS\LAB-01-programacion-basica-en-python-Jaffet18\files\input\data.csv'

    # Abrir el archivo y leer línea por línea
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones y obtener la segunda columna (índice 1)
            columnas = linea.split('\t')
            try:
                # Agregar el elemento a la lista sin cambiar su tipo
                elementos_columna_dos.append(columnas[1])
            except IndexError:
                # Manejar el caso donde la columna no existe
                continue

    print(elementos_columna_dos)

    # Convertir los elementos de la lista a enteros
    elementos_columna_dos_enteros = [int(elemento) for elemento in elementos_columna_dos]

    suma_elementos_columna_dos = sum(elementos_columna_dos_enteros)

    print(elementos_columna_dos_enteros)
    print(suma_elementos_columna_dos)

    return suma_elementos_columna_dos

print(pregunta_01())

