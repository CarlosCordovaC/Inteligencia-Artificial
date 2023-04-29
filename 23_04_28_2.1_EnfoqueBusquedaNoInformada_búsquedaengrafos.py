# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:45:35 2023

@author: carlo

Un ejemplo de la vida diaria donde se puede aplicar la búsqueda en grafos es la navegación
en Internet. Los sitios web pueden ser modelados como nodos en un grafo, y los enlaces entre 
ellos como aristas. La búsqueda en grafos se utiliza en los motores de búsqueda para encontrar 
páginas web relevantes para una consulta de búsqueda específica. El motor de búsqueda comienza
en un nodo inicial que contiene los resultados de la búsqueda y luego sigue los enlaces a 
otros nodos relevantes hasta encontrar el nodo objetivo que contiene la respuesta a la 
consulta.

búsqueda en grafos
"""

from collections import deque

# Definir el grafo
grafo = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Función de búsqueda en grafos no informada
def busqueda_en_grafos_no_informada(grafo, inicio, objetivo):
    cola = deque([inicio])
    visitado = set()

    while cola:
        nodo = cola.popleft()

        if nodo == objetivo:
            return True

        if nodo in visitado:
            continue

        visitado.add(nodo)

        for vecino in grafo[nodo]:
            if vecino not in visitado:
                cola.append(vecino)

    return False

# Ejecución de la búsqueda en grafos no informada
inicio = 'A'
objetivo = 'F'
resultado = busqueda_en_grafos_no_informada(grafo, inicio, objetivo)

# Imprimir resultado
if resultado:
    print(f"Se encontró una ruta de {inicio} a {objetivo}.")
else:
    print(f"No se encontró una ruta de {inicio} a {objetivo}.")


"""
En este ejemplo, el grafo se define como un diccionario de conjuntos, donde las claves 
son los nodos y los valores son los nodos vecinos. La función 
busqueda_en_grafos_no_informada realiza una búsqueda en profundidad en el grafo, 
utilizando una cola para almacenar los nodos que aún no se han visitado. La función 
devuelve True si se encuentra una ruta del nodo de inicio al nodo objetivo, y False 
en caso contrario.
"""