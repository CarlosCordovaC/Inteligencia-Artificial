# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:08:03 2023

@author: carlo

Un ejemplo de Búsqueda de Haz Local que se puede aplicar a la vida diaria es encontrar 
la mejor ruta para llegar a un destino en un mapa. En lugar de explorar todas las rutas 
posibles, el algoritmo de Haz Local solo considera un número limitado de rutas a la vez 
y, a través de iteraciones, se expande en diferentes rutas para encontrar la mejor opción. 
Esto puede ser útil cuando se tiene prisa y se desea encontrar la ruta más rápida posible, 
aunque no garantiza que sea la mejor opción en términos de distancia o tráfico.

Búsqueda de Haz Local
"""

import random

# Definir la función a maximizar
def f(x):
    return -x**2 + 10*x + 100

# Definir los parámetros del algoritmo
num_rays = 10
num_selected = 3
num_new_rays = 5
max_iterations = 100

# Generar los rayos iniciales
rays = [random.uniform(0, 10) for _ in range(num_rays)]

# Empezar la búsqueda
for i in range(max_iterations):
    # Evaluar la función en cada rayo
    values = [f(x) for x in rays]

    # Seleccionar los mejores rayos
    selected_indices = sorted(range(len(values)), key=lambda i: values[i], reverse=True)[:num_selected]
    selected_rays = [rays[i] for i in selected_indices]

    # Generar nuevos rayos a partir de los seleccionados
    new_rays = []
    for j in range(num_new_rays):
        for ray in selected_rays:
            new_rays.append(ray + random.uniform(-1, 1))
    rays = selected_rays + new_rays

# Encontrar el máximo
max_value = max([f(x) for x in rays])
max_x = [x for x in rays if f(x) == max_value][0]

print("El máximo de la función f(x) se alcanza en x =", max_x, "con un valor de f(x) =", max_value)


"""
En este ejemplo, el algoritmo comienza generando 10 rayos aleatorios en el 
intervalo [0, 10]. Luego, en cada iteración, evalúa la función en cada rayo, 
selecciona los 3 mejores y genera 5 nuevos rayos a partir de ellos. Después de 
100 iteraciones, el algoritmo encuentra el máximo de la función, que en este caso 
es x=5 con un valor de f(x)=125.
"""