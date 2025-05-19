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
    # ruta_archivo = r'https://github.com/2025-1-analitica-descriptiva/LAB-01-programacion-basica-en-python-Jaffet18/tree/main/files/input'

    # Abrir el archivo y leer línea por línea
    # Se utiliza la ruta relativa para abrir el archivo
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea por tabulaciones
            columnas = linea.split('\t')
            try:
                # Agregar el elemento a la lista
                elementos_columna_dos.append(columnas[1])
            except IndexError:
                continue

    print(elementos_columna_dos)

    elementos_columna_dos_enteros = [int(elemento) for elemento in elementos_columna_dos]

    suma_elementos_columna_dos = sum(elementos_columna_dos_enteros)

    print(elementos_columna_dos_enteros)
    print(suma_elementos_columna_dos)

    return suma_elementos_columna_dos

print(pregunta_01())

