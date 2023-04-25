# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:03:11 2023

@author: carlo

Busqueda no informada 
"""

import networkx as nx

# Crear un grafo aleatorio con NetworkX
graph = nx.gnm_random_graph(10, 20)

# Seleccionar un nodo de inicio y un nodo de destino aleatorios
start_node = 1
goal_node = 8

# Función de búsqueda no informada
def uninformed_search(graph, start, goal):
    # Inicializar la frontera con el nodo de inicio
    frontier = [start]

    # Inicializar el conjunto de nodos visitados
    visited = set()

    while frontier:
        # Sacar el primer nodo de la frontera
        node = frontier.pop(0)

        # Si el nodo es el objetivo, retornar la ruta
        if node == goal:
            return visited

        # Si el nodo no es el objetivo, agregarlo al conjunto de nodos visitados
        visited.add(node)

        # Agregar todos los vecinos del nodo a la frontera
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                frontier.append(neighbor)

    # Si no se encuentra una ruta, retornar None
    return None

# Ejecutar la búsqueda no informada
path = uninformed_search(graph, start_node, goal_node)

# Imprimir el resultado
if path:
    print("Se encontró una ruta desde", start_node, "hasta", goal_node, ":", path)
else:
    print("No se encontró una ruta desde", start_node, "hasta", goal_node)

