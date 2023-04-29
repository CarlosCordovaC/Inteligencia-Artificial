# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:01:50 2023

@author: carlo

Un ejemplo de la vida cotidiana de la búsqueda en profundidad limitada puede ser 
la búsqueda de un objeto perdido en una casa. En lugar de buscar en profundidad cada 
habitación y cada objeto en cada habitación, se puede establecer un límite de profundidad 
en la exploración de las habitaciones y priorizar la búsqueda en áreas más prometedoras o 
relevantes. Por ejemplo, si el objeto perdido es un libro, es más probable que se encuentre 
en la sala de estar o en la biblioteca que en la cocina o en el baño.

Búsqueda en Profundidad Limitada
"""

def find_path_dfs_limited(graph, start, end, limit):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (node, path) = stack.pop()
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            if limit > 0:
                for next_node in graph[node]:
                    if next_node not in visited:
                        stack.append((next_node, path + [next_node]))
            limit -= 1
    return None

maze = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': ['L'],
    'I': ['M'],
    'J': ['N'],
    'K': ['O'],
    'L': ['P'],
    'M': ['Q'],
    'N': ['R'],
    'O': ['S'],
    'P': ['T'],
    'Q': [],
    'R': [],
    'S': [],
    'T': []
}

start = 'A'
end = 'T'
limit = 6

path = find_path_dfs_limited(maze, start, end, limit)

if path is not None:
    print(f'El camino más corto desde {start} a {end} es: {path}')
else:
    print(f'No se encontró un camino desde {start} a {end} dentro del límite de profundidad {limit}')


"""
En este ejemplo, el laberinto se representa como un diccionario en el que cada clave es 
un nodo y su valor es una lista de los nodos a los que está conectado. La función 
find_path_dfs_limited realiza la búsqueda en profundidad limitada desde el nodo de 
inicio hasta el nodo de destino, evitando que la búsqueda se adentre más allá de un
límite determinado de profundidad. El límite de profundidad se reduce en cada iteración, 
lo que asegura que la búsqueda no se prolongue indefinidamente.

"""