# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:09:16 2023

@author: carlo

Por ejemplo, se puede utilizar la búsqueda en profundidad iterativa para encontrar el 
camino más corto para salir de un laberinto. Imagine que está en un laberinto y quiere 
encontrar la salida más cercana. Comenzaría en su posición actual y trataría de explorar 
todas las opciones posibles. Si no encuentra una salida en el primer intento, volvería a 
su posición original y comenzaría a explorar las opciones nuevamente, pero esta vez iría 
un nivel más profundo. Continuaría haciendo esto hasta encontrar la salida más cercana.

búsqueda en profundidad iterativa

"""

import random

# Generar lista de números aleatorios
numeros = [random.randint(1, 1000) for i in range(100)]

# Función de búsqueda en profundidad iterativa
def busqueda_profundidad_iterativa(lista, objetivo):
    for profundidad_limite in range(len(lista)):
        resultado = busqueda_profundidad_limitada(lista, objetivo, profundidad_limite)
        if resultado is not None:
            return resultado
    return None

def busqueda_profundidad_limitada(lista, objetivo, profundidad_limite):
    resultado = None
    if profundidad_limite == 0:
        if lista and lista[0] == objetivo:
            resultado = lista[0]
    else:
        for i in range(len(lista)):
            if lista[i] == objetivo:
                resultado = lista[i]
            else:
                sub_lista = lista[i+1:]
                sub_resultado = busqueda_profundidad_limitada(sub_lista, objetivo, profundidad_limite-1)
                if sub_resultado is not None:
                    resultado = sub_resultado
            if resultado is not None:
                break
    return resultado


# Ejecución de la búsqueda en profundidad iterativa
objetivo = 500
resultado = busqueda_profundidad_iterativa(numeros, objetivo)

# Imprimir resultado
if resultado is not None:
    print("El número más cercano a 500 es:", resultado)
else:
    print("No se encontró un número cercano a 500 en la lista.")

"""
En este ejemplo, la función busqueda_profundidad_iterativa realiza una búsqueda en 
profundidad iterativa en una lista de números aleatorios para encontrar el número más 
cercano a 500. La función utiliza la función busqueda_profundidad_limitada para realizar 
la búsqueda en profundidad limitada en cada iteración, incrementando la profundidad límite 
en cada iteración hasta que se encuentra el objetivo o se alcanza la profundidad máxima.

La función busqueda_profundidad_limitada utiliza recursión para realizar una búsqueda en 
profundidad limitada en la lista. La profundidad límite se va reduciendo en cada llamada 
recursiva hasta que se alcanza el límite de profundidad o se encuentra el objetivo.
"""
