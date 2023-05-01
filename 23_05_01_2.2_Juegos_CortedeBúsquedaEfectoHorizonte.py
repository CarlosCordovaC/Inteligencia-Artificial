# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:31:42 2023

@author: carlo

En la vida diaria, se pueden encontrar ejemplos de corte de búsqueda en situaciones en 
las que hay demasiadas opciones a considerar. Por ejemplo, al planificar una dieta saludable, 
puede haber muchas opciones diferentes a considerar, como el tipo de alimentos, la cantidad 
de calorías y la frecuencia de las comidas. Es posible que no sea posible considerar todas 
las opciones posibles, por lo que se pueden establecer límites en la cantidad de tiempo y 
recursos que se dedican a la planificación de la dieta, o en el número de opciones que se 
consideran. Esto puede ayudar a reducir la complejidad de la tarea y a llegar a una solución 
satisfactoria en un plazo razonable.

Corte de Búsqueda: Efecto Horizonte
"""

def dfs(node, graph, goal, visited, limit):
    """
    Búsqueda en profundidad limitada
    """
    if node == goal:
        return [node]
    if limit == 0:
        return None
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            path = dfs(neighbor, graph, goal, visited, limit-1)
            if path:
                return [node] + path
    return None

def iddfs(start, graph, goal, max_depth):
    """
    Búsqueda en profundidad iterativa
    """
    for depth in range(max_depth):
        visited = []
        path = dfs(start, graph, goal, visited, depth)
        if path:
            return path
    return None

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': []
}

start = 'A'
goal = 'H'
max_depth = 5
path = iddfs(start, graph, goal, max_depth)

print(path)
