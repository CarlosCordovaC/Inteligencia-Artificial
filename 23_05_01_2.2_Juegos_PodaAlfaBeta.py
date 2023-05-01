# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:56:36 2023

@author: carlo

El algoritmo de poda alfa-beta funciona mediante la comparación de los valores de dos 
variables, "alfa" y "beta", que representan los límites inferior y superior del valor de 
la solución. Durante la búsqueda, se actualizan estos valores en función de los nodos 
evaluados. Si el valor de un nodo es mayor que beta (en el caso del jugador Maximizador) 
o menor que alfa (en el caso del jugador Minimizador), se puede descartar ese nodo y 
todos los nodos hijos que se generen a partir de él. Esto se conoce como "poda" del árbol 
de búsqueda.

Poda Alfa-Beta
"""

# Definir un árbol de búsqueda
arbol = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': [1, 2, 3],
    'F': [4, 5, 6],
    'G': [7, 8, 9],
    'H': [10, 11, 12],
    'I': [13, 14, 15],
    'J': [16, 17, 18]
}

# Definir la función de evaluación
def evaluar_nodo(nodo):
    if isinstance(nodo, int):
        return nodo
    else:
        return max(evaluar_nodo(hijo) for hijo in arbol[nodo])

# Definir la función minimax con poda alfa-beta
def minimax(nodo, profundidad, alfa, beta, maximizar):
    if profundidad == 0 or isinstance(nodo, int):
        return evaluar_nodo(nodo)

    if maximizar:
        mejor_valor = float("-inf")
        for hijo in arbol[nodo]:
            valor = minimax(hijo, profundidad-1, alfa, beta, False)
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for hijo in arbol[nodo]:
            valor = minimax(hijo, profundidad-1, alfa, beta, True)
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor

# Buscar el mejor movimiento en el árbol de búsqueda
mejor_movimiento = None
mejor_valor = float("-inf")
for hijo in arbol['A']:
    valor = minimax(hijo, 3, float("-inf"), float("inf"), False)
    if valor > mejor_valor:
        mejor_valor = valor
        mejor_movimiento = hijo

print("El mejor movimiento es:", mejor_movimiento)
print("Su valor es:", mejor_valor)
