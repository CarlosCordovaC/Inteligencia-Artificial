# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:29:23 2023

@author: carlo
Un ejemplo de cómo se puede aplicar A* en la vida diaria es en la planificación de un 
viaje en una ciudad desconocida. Supongamos que desea encontrar la mejor ruta para ir 
desde su hotel a un museo. Puede representar las calles y las intersecciones como un 
grafo, donde cada intersección es un nodo y cada calle es un borde. La búsqueda A* puede 
ser utilizada para encontrar el camino más corto y eficiente para llegar al museo desde 
su hotel, considerando el tráfico y la distancia.

La función de evaluación se define como f(n) = g(n) + h(n). 
A* busca expandir el nodo con el valor de f más bajo en la frontera en 
cada iteración. Es un algoritmo completo y óptimo, lo que significa que siempre 
encontrará la solución óptima si existe y no se expandirán nodos innecesarios.

Búsquedas A* y AO*
"""

import heapq

# Definimos la función de búsqueda A*
def A_star(graph, start, goal):
    # Creamos las estructuras de datos necesarias
    open_set = []
    heapq.heappush(open_set, (0, start))
    closed_set = set()
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {} # definimos la variable came_from

    # Empezamos la búsqueda
    while open_set:
        current = heapq.heappop(open_set)[1]

        # Si encontramos el objetivo, devolvemos la ruta
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Expandimos los nodos adyacentes
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]

            # Si el nodo ya ha sido visitado con menor costo, lo ignoramos
            if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            # Si encontramos un camino más corto, lo actualizamos
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    closed_set.add(neighbor)

    # Si no encontramos un camino, devolvemos None
    return None

# Definimos una función heurística (en este caso, distancia euclidiana)
def heuristic(node, goal):
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

# Ejemplo de uso
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (1, 2): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1},
}

start = (0, 0)
goal = (1, 2)

path = A_star(graph, start, goal)
print(path)


"""
Este código implementa el algoritmo de búsqueda A* para encontrar la ruta más corta desde 
un nodo inicial hasta un nodo objetivo en un grafo ponderado. El grafo se representa 
mediante un diccionario de diccionarios, donde las claves del diccionario exterior son 
los nodos del grafo, y los valores son diccionarios que representan los vecinos del nodo 
y el costo de llegar a ellos.

La función devuelve la ruta más corta desde el nodo inicial hasta el nodo objetivo, 
representada como una lista de nodos, o None si no se encontró una ruta. El camino se 
devuelve siguiendo los nodos desde el objetivo hasta el nodo inicial, utilizando un 
diccionario came_from que almacena los padres de cada nodo en el camino más corto.

"""