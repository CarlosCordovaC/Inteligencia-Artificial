# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:41:33 2023

@author: carlo

Supongamos que una empresa de mensajería tiene que entregar varios paquetes a 
diferentes destinos. Cada destino tiene una ubicación específica y un costo asociado 
para entregar el paquete a ese destino. El objetivo es encontrar una ruta óptima que
 minimice el costo total de la entrega de todos los paquetes.
"""
from queue import PriorityQueue

# Creamos el grafo
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

# Función de búsqueda por costo uniforme
def busqueda_costo_uniforme(grafo, inicio, objetivo):
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, inicio))
    visitado = set()

    while not cola_prioridad.empty():
        costo, nodo_actual = cola_prioridad.get()
        if nodo_actual == objetivo:
            return costo
        if nodo_actual in visitado:
            continue
        visitado.add(nodo_actual)
        for vecino, costo_arista in grafo[nodo_actual].items():
            if vecino not in visitado:
                cola_prioridad.put((costo + costo_arista, vecino))

# Ejemplo de uso
costo = busqueda_costo_uniforme(grafo, 'A', 'E')
print(f"El costo mínimo desde 'A' hasta 'E' es {costo}.")
"""
Este código define el grafo como un diccionario de diccionarios, y define una 
función busqueda_costo_uniforme que toma como entrada el grafo, el nodo inicial 
y el nodo objetivo, y utiliza una cola de prioridad para realizar la búsqueda por 
costo uniforme. Luego, se utiliza el grafo y la función para encontrar el costo 
mínimo de llegar desde el nodo 'A' hasta el nodo 'E'.
"""