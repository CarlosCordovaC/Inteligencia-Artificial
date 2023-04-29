# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:35:16 2023

@author: carlo

Búsqueda en Anchura
"""
from collections import deque

# Definir el grafo como un diccionario de listas de adyacencia
grafo = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': ['G'],
         'E': [],
         'F': ['H', 'I'],
         'G': [],
         'H': [],
         'I': ['J'],
         'J': []}

# Función para realizar la búsqueda en anchura
def bfs(grafo, inicio, objetivo):
    # Cola para almacenar los nodos a visitar
    cola = deque([inicio])
    # Diccionario para almacenar el camino recorrido
    padres = {inicio: None}

    while cola:
        actual = cola.popleft()
        if actual == objetivo:
            # Si encontramos el objetivo, construir el camino y retornarlo
            camino = [objetivo]
            while actual != inicio:
                actual = padres[actual]
                camino.append(actual)
            camino.reverse()
            return camino
        for vecino in grafo[actual]:
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)

    # Si no encontramos el objetivo, retornar None
    return None

# Ejemplo de uso
inicio = 'A'
objetivo = 'J'
camino = bfs(grafo, inicio, objetivo)
if camino:
    print(f"El camino más corto entre {inicio} y {objetivo} es: {', '.join(camino)}")
else:
    print(f"No se encontró un camino entre {inicio} y {objetivo}")
