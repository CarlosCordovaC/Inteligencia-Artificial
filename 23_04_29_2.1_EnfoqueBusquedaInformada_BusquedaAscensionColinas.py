# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:55:38 2023

@author: carlo

Un ejemplo de la Búsqueda de Ascensión de Colinas en la vida cotidiana puede ser en 
la planificación de una dieta saludable. En este caso, se podría utilizar la Búsqueda 
de Ascensión de Colinas con enfoque hacia la Búsqueda Informada para encontrar una dieta 
que minimice el consumo de calorías y maximice el consumo de nutrientes esenciales. 
La información heurística podría incluir la cantidad de calorías y nutrientes en los 
diferentes alimentos, así como las necesidades nutricionales individuales de la persona 
que sigue la dieta. El algoritmo podría comenzar con una dieta aleatoria y examinar las 
dietas vecinas para encontrar una mejor solución, y así sucesivamente hasta encontrar una 
dieta óptima.

Búsqueda de Ascensión de Colinas
"""

import math

# Definimos la función objetivo
def f(x):
    return math.sin(x) + math.sin(10*x/3)

# Definimos la función de búsqueda de ascenso de colinas
def hill_climbing(f, x0, delta=0.01, max_iter=100):
    x = x0
    fx = f(x)
    for i in range(max_iter):
        x1 = x + delta
        x2 = x - delta
        if f(x1) > fx:
            x = x1
            fx = f(x)
        elif f(x2) > fx:
            x = x2
            fx = f(x)
        else:
            break
    return x, fx

# Ejemplo de uso
x0 = 0.5
x, fx = hill_climbing(f, x0)
print("x = {}, f(x) = {}".format(x, fx))


"""
En este ejemplo, la función objetivo es f(x) = sin(x) + sin(10x/3), y queremos encontrar 
el valor de x que maximiza la función. La función de búsqueda de ascenso de colinas toma 
como argumentos la función objetivo f, un valor inicial x0, una longitud de paso delta y 
un número máximo de iteraciones max_iter. En cada iteración, la función evalúa la función 
objetivo en dos puntos cercanos a x (uno a la derecha y otro a la izquierda) y se mueve 
hacia el punto que produce un valor más alto de la función objetivo. El proceso se repite 
hasta que no se puede encontrar un punto mejor.
"""
