# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:36:53 2023

@author: carlo

En inteligencia artificial, la Búsqueda de Temple Simulado se utiliza para resolver 
problemas en los que no hay una solución clara, pero se tiene una idea general de lo 
que se quiere lograr. Por ejemplo, se puede utilizar para diseñar circuitos electrónicos 
o para optimizar rutas de transporte.

Temple Simulado
"""

import random
import math

# Distancias entre ciudades
distancias = [[0, 10, 15, 20],
              [10, 0, 35, 25],
              [15, 35, 0, 30],
              [20, 25, 30, 0]]

# Lista de ciudades
ciudades = [0, 1, 2, 3]

# Función para calcular la distancia total de una ruta
def calcular_distancia(ruta):
    distancia_total = 0
    for i in range(len(ruta)-1):
        distancia_total += distancias[ruta[i]][ruta[i+1]]
    distancia_total += distancias[ruta[-1]][ruta[0]]
    return distancia_total

# Solución inicial aleatoria
ruta_actual = ciudades.copy()
random.shuffle(ruta_actual)
mejor_ruta = ruta_actual.copy()
mejor_distancia = calcular_distancia(mejor_ruta)

# Parámetros de la búsqueda
temperatura_inicial = 100
factor_enfriamiento = 0.99
max_iteraciones = 1000

# Búsqueda de temple simulado
temperatura = temperatura_inicial
for i in range(max_iteraciones):
    # Generar una solución vecina
    vecino = ruta_actual.copy()
    a = random.randint(0, len(ciudades)-1)
    b = random.randint(0, len(ciudades)-1)
    vecino[a], vecino[b] = vecino[b], vecino[a]
    
    # Calcular la diferencia de distancia entre la solución actual y la vecina
    distancia_actual = calcular_distancia(ruta_actual)
    distancia_vecino = calcular_distancia(vecino)
    diferencia_distancia = distancia_vecino - distancia_actual
    
    # Si la solución vecina es mejor, se actualiza la mejor solución
    if diferencia_distancia < 0:
        ruta_actual = vecino.copy()
        if distancia_vecino < mejor_distancia:
            mejor_ruta = ruta_actual.copy()
            mejor_distancia = distancia_vecino
    # Si la solución vecina es peor, se acepta con cierta probabilidad
    else:
        probabilidad_aceptacion = math.exp(-diferencia_distancia / temperatura)
        if random.random() < probabilidad_aceptacion:
            ruta_actual = vecino.copy()
    
    # Enfriar la temperatura
    temperatura *= factor_enfriamiento

# Imprimir la mejor solución encontrada
print("La mejor ruta encontrada es:", mejor_ruta, "con una distancia de", mejor_distancia)

"""
En este ejemplo, se utiliza la búsqueda de temple simulado para encontrar la ruta 
más corta que visite cada ciudad exactamente una vez y vuelva al punto de partida. 
La solución inicial se genera de forma aleatoria y luego se van generando soluciones 
vecinas intercambiando dos ciudades aleatorias en la ruta actual. Si la solución vecina 
es mejor que la actual, se actualiza la mejor solución. Si la solución vecina es peor, 
se acepta con una cierta probabilidad determinada por la temperatura actual. 

"""