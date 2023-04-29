# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:07:05 2023

@author: carlo
La búsqueda tabú podría ayudarte a encontrar la mejor combinación de destino, fechas y 
duración que se ajuste a tus restricciones y maximice tu experiencia de vacaciones 
dentro de tu presupuesto limitado. Por ejemplo, podrías usar una lista tabú para evitar 
seleccionar las mismas fechas o destinos dos veces seguidas, o para evitar seleccionar 
destinos que ya has visitado en el pasado.

Búsqueda Tabú
"""
import random

# Definir los datos del problema de la mochila
pesos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
peso_maximo = 50

# Definir los parámetros de la Búsqueda Tabú
tabu_size = 10
max_iterations = 1000

# Inicializar la solución actual y la mejor solución
n = len(pesos)
solucion_actual = [0] * n
mejor_solucion = [0] * n
mejor_valor = 0

# Inicializar la lista tabú
tabu_list = []

# Empezar la búsqueda
iteraciones = 0
while iteraciones < max_iterations:
    # Generar una lista de vecinos
    vecinos = [list(solucion_actual) for _ in range(n)]
    for i in range(n):
        vecinos[i][i] = 1 - vecinos[i][i]

    # Calcular la función de evaluación para cada vecino
    valores_vecinos = [sum(valores[j] for j in range(n) if vecinos[i][j]) for i in range(n)]
    pesos_vecinos = [sum(pesos[j] for j in range(n) if vecinos[i][j]) for i in range(n)]
    penalizaciones_vecinos = [max(0, pesos_vecinos[i] - peso_maximo) for i in range(n)]
    evaluaciones_vecinos = [valores_vecinos[i] - penalizaciones_vecinos[i] for i in range(n)]

    # Encontrar el mejor vecino que no esté en la lista tabú
    mejor_vecino = max((i for i in range(n) if vecinos[i] not in tabu_list), key=lambda i: evaluaciones_vecinos[i], default=None)

    # Actualizar la solución actual y la mejor solución
    solucion_actual = vecinos[mejor_vecino] if mejor_vecino is not None else solucion_actual
    valor_actual = evaluaciones_vecinos[mejor_vecino] if mejor_vecino is not None else mejor_valor
    if valor_actual > mejor_valor:
        mejor_solucion = list(solucion_actual)
        mejor_valor = valor_actual

    # Añadir la solución actual a la lista tabú
    tabu_list.append(list(solucion_actual))
    if len(tabu_list) > tabu_size:
        tabu_list.pop(0)

    # Incrementar el número de iteraciones
    iteraciones += 1

print(f"La mejor solución encontrada tiene un valor de {mejor_valor} y se compone de los siguientes objetos:")
for i, incluido in enumerate(mejor_solucion):
    if incluido:
        print(f" - Objeto {i+1} con peso {pesos[i]} y valor {valores[i]}")


"""
El problema de la mochila es un problema de optimización combinatoria en el que se trata de 
llenar una mochila con objetos de diferentes pesos y valores. El objetivo es maximizar el 
valor total de los objetos que se pueden llevar en la mochila sin superar un peso máximo 
dado.

En este ejemplo, vamos a resolver un problema de la mochila con 10 objetos, un peso máximo 
de 50 y una duración máxima de 1000 iteraciones. Utilizaremos una estrategia de Búsqueda 
Tabú para explorar el espacio de soluciones y encontrar la mejor solución posible.
"""