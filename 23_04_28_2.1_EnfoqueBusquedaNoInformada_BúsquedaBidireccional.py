# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:32:47 2023

@author: carlo

Un ejemplo de búsqueda bidireccional que se puede aplicar a la vida diaria es la búsqueda 
de pareja. En lugar de buscar a una pareja desde un único punto de partida, se pueden 
utilizar dos puntos de partida diferentes: uno desde el propio círculo social y otro desde 
un círculo social diferente, como una aplicación de citas en línea. De esta manera, 
se pueden expandir las posibilidades de encontrar una pareja compatible y aumentar las 
probabilidades de éxito en la búsqueda.

búsqueda bidireccional
"""

import random

# Generar lista de números aleatorios
numeros = [random.randint(1, 1000) for i in range(100)]

# Función de búsqueda bidireccional
def busqueda_bidireccional(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        if lista[inicio] == objetivo:
            return lista[inicio]
        if lista[fin] == objetivo:
            return lista[fin]
        inicio += 1
        fin -= 1
    return None

# Ejecución de la búsqueda bidireccional
objetivo = 500
resultado = busqueda_bidireccional(numeros, objetivo)

# Imprimir resultado
if resultado is not None:
    print("El número más cercano a 500 es:", resultado)
else:
    print("No se encontró un número cercano a 500 en la lista.")

"""
En este ejemplo, la función busqueda_bidireccional recibe como parámetros una lista 
de números y un objetivo, y utiliza un enfoque bidireccional para buscar el número más 
cercano al objetivo en la lista. La función comienza por los extremos de la lista y se 
mueve hacia el centro, buscando el objetivo en cada iteración. Si encuentra el objetivo 
en alguno de los extremos, devuelve ese número. Si la búsqueda no encuentra el objetivo 
en la lista, devuelve None.
"""