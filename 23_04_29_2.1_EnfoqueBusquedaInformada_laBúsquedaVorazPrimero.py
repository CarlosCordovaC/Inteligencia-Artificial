# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:52:12 2023

@author: carlo

Un ejemplo de cómo se podría utilizar la Búsqueda Voraz Primero en la vida diaria es 
en la búsqueda de un artículo en un supermercado. Supongamos que se busca un artículo 
específico, como un paquete de galletas, en un supermercado desconocido. Uno podría utilizar 
la técnica de Búsqueda Voraz Primero para buscar el pasillo más cercano a la entrada que 
tenga galletas, asumiendo que el pasillo más cercano a la entrada es el más probable que 
tenga las galletas. De esta manera, se podría encontrar el artículo deseado de manera más 
rápida y eficiente. Sin embargo, existe la posibilidad de que se ignoren otros pasillos que 
también tienen galletas, pero que no son tan cercanos a la entrada.

la Búsqueda Voraz Primero
"""

import heapq

# Definimos el grafo en forma de diccionario
grafo = {'A': {'B': 5, 'C': 7},
         'B': {'D': 3, 'E': 2},
         'C': {'E': 1},
         'D': {'F': 2},
         'E': {'G': 5},
         'F': {},
         'G': {}}

# Función de búsqueda voraz primero
def buscar_voraz_primero(grafo, inicio, objetivo):
    frontera = [(heuristica(inicio, objetivo), inicio)]
    visitados = set()

    while frontera:
        _, actual = heapq.heappop(frontera)
        if actual == objetivo:
            return True
        visitados.add(actual)
        for vecino in grafo[actual]:
            if vecino not in visitados:
                heapq.heappush(frontera, (heuristica(vecino, objetivo), vecino))

    return False

# Función heurística (distancia recta entre dos nodos)
def heuristica(nodo, objetivo):
    coordenadas = {'A': (0, 0), 'B': (1, 0), 'C': (0, 1), 'D': (2, 0), 'E': (1, 1), 'F': (3, 0), 'G': (2, 1)}
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return abs(x1 - x2) + abs(y1 - y2)

# Ejemplo de uso
buscar_voraz_primero(grafo, 'A', 'F')


"""
En este ejemplo, la función heurística calcula la distancia recta entre dos nodos en 
una matriz de coordenadas y la devuelve como resultado. Este tipo de heurística es común 
en la implementación de algoritmos de búsqueda voraz primero.

En general, la búsqueda voraz primero se utiliza en problemas de optimización en los 
que se tiene una solución aproximada a priori y se busca mejorarla. Por ejemplo, en la 
planificación de rutas, donde se conoce el destino pero no la ruta óptima.
"""