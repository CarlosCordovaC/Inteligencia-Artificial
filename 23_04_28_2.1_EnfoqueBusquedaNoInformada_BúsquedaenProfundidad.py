# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:52:14 2023

@author: carlo
Un ejemplo de búsqueda en profundidad que se puede aplicar a la vida diaria es la 
búsqueda de un objeto perdido en una casa. Supongamos que se ha perdido un anillo en 
una casa y se quiere encontrarlo. En lugar de buscar en cada habitación de la casa al 
mismo tiempo, la búsqueda en profundidad implicaría comenzar en una habitación y revisarla 
completamente antes de pasar a la siguiente habitación. Si no se encuentra el anillo en 
la primera habitación, se pasaría a la siguiente y así sucesivamente hasta que se encuentre 
el anillo o se hayan explorado todas las habitaciones.

búsqueda en profundidad
"""

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

def busqueda_profundidad(grafo, inicio, destino, visitados=[]):
    visitados.append(inicio)
    
    if inicio == destino:
        return visitados
    
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            resultado = busqueda_profundidad(grafo, vecino, destino, visitados)
            if resultado is not None:
                return resultado
    
    return None

resultado = busqueda_profundidad(grafo, 'A', 'D')
print(resultado)


"""
En este ejemplo, la función busqueda_profundidad toma el grafo, el nodo de inicio, 
el nodo de destino y una lista de nodos visitados (que por defecto está vacía). 
En cada llamada recursiva, se agrega el nodo actual a la lista de visitados y se 
comprueba si es el nodo de destino. Si es el nodo de destino, se devuelve la lista 
de nodos visitados. Si no es el nodo de destino, se recorre la lista de nodos adyacentes 
y se llama recursivamente a la función para cada uno de ellos que no haya sido 
visitado todavía. Si se encuentra un camino que llega al nodo de destino, se devuelve la 
lista de nodos visitados. Si no se encuentra ningún camino, se devuelve None.

En este ejemplo, la búsqueda en profundidad encuentra un camino desde el nodo 
'A' al nodo 'D', que es ['A', 'B', 'D'].
"""