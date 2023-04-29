# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:16:01 2023

@author: carlo

Un ejemplo de la vida diaria en el que se pueden utilizar los Algoritmos Genéticos es en 
la selección de los mejores ingredientes para una receta de cocina. Supongamos que queremos 
crear la mejor receta de pastel de chocolate posible. Podríamos utilizar un Algoritmo 
Genético para generar una población inicial de ingredientes aleatorios (por ejemplo, 
harina, azúcar, huevos, cacao, leche, etc.), evaluar la calidad de cada receta de pastel de 
chocolate resultante, seleccionar las más exitosas y combinarlas entre sí para generar una 
nueva población de recetas aún más exitosas. Este proceso se repetiría varias veces hasta que 
se obtuviera una receta óptima en términos de sabor, textura y presentación.

Algoritmos Genéticos
"""

import random

# Función objetivo
def fitness_func(x):
    return x**2 - 3*x + 4

# Parámetros del algoritmo genético
pop_size = 100
num_generations = 50
mutation_rate = 0.1
tournament_size = 5

# Generar población inicial
population = [random.uniform(0, 5) for _ in range(pop_size)]

# Bucle de evolución
for generation in range(num_generations):
    # Evaluar aptitud
    fitness_scores = [fitness_func(x) for x in population]

    # Seleccionar padres
    parents = []
    for _ in range(pop_size):
        tournament = random.sample(fitness_scores, tournament_size)
        winner = max(tournament)
        parent = population[fitness_scores.index(winner)]
        parents.append(parent)

    # Crear nueva población a través de cruzamiento y mutación
    new_population = []
    for _ in range(pop_size):
        parent_1 = random.choice(parents)
        parent_2 = random.choice(parents)
        child = (parent_1 + parent_2) / 2.0
        if random.random() < mutation_rate:
            child += random.uniform(-0.1, 0.1)
        new_population.append(child)

    # Actualizar la población
    population = new_population

# Encontrar la mejor solución
fitness_scores = [fitness_func(x) for x in population]
best_fitness = max(fitness_scores)
best_index = fitness_scores.index(best_fitness)
best_solution = population[best_index]

# Imprimir la mejor solución
print("La solución óptima es: x = ", best_solution)
print("El valor óptimo es: f(x) = ", best_fitness)


"""
Supongamos que queremos encontrar el máximo de la función f(x) = x^2 - 3x + 4 en el 
intervalo [0, 5]. Podemos usar un algoritmo genético para encontrar el valor de x que 
maximiza esta función.

Primero, definimos nuestra población inicial como un conjunto aleatorio de valores de x 
en el intervalo [0, 5]. Luego, evaluamos la función de aptitud (fitness function) de cada 
miembro de la población, que en este caso es simplemente el valor de f(x) para cada valor 
de x. A continuación, seleccionamos a los padres para la siguiente generación utilizando 
un método de selección de torneos. Después, creamos una nueva población cruzando los padres
 seleccionados y aplicando una mutación aleatoria a algunos de los miembros de la 
 nueva población. Repetimos este proceso durante un número fijo de generaciones y 
 seleccionamos al miembro con la mayor aptitud como la solución óptima.
"""