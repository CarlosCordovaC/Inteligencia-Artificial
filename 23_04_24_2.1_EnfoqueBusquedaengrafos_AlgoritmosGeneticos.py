# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:25:30 2023

@author: carlo
"""

import random

# Definición del grafo
graph = {
    'A': [('B', 7), ('C', 3)],
    'B': [('A', 7), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 2), ('C', 2), ('E', 4)],
    'E': [('D', 4)]
}

# Función objetivo, en este caso, encontrar la ruta más corta entre dos nodos del grafo
def fitness(route):
    total_distance = 0
    for i in range(len(route) - 1):
        node1 = route[i]
        node2 = route[i + 1]
        for neighbor, distance in graph[node1]:
            if neighbor == node2:
                total_distance += distance
    return total_distance

# Función de selección de padres (selecciona dos individuos para cruzamiento)
def selection(population, fitness_func):
    fitnesses = [fitness_func(individual) for individual in population]
    max_fitness = max(fitnesses)
    pool = [population[i] for i in range(len(population)) if fitnesses[i] == max_fitness]
    return random.choice(pool), random.choice(pool)

# Función de cruzamiento (crea un nuevo individuo a partir de dos padres)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child = parent1[:crossover_point]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

# Función de mutación (modifica un gen del individuo)
def mutation(individual):
    mutation_point1 = random.randint(0, len(individual) - 1)
    mutation_point2 = random.randint(0, len(individual) - 1)
    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual

# Algoritmo genético
def genetic_algorithm(population_size, fitness_func, selection_func, crossover_func, mutation_func, num_generations):
    # Generación de la población inicial (individuos aleatorios)
    population = [list(graph.keys()) for i in range(population_size)]
    for i in range(num_generations):
        # Evaluación del fitness de cada individuo
        fitnesses = [fitness_func(individual) for individual in population]
        # Selección de padres
        parent1, parent2 = selection_func(population, fitness_func)
        # Cruzamiento y mutación para generar nuevos individuos
        children = [crossover_func(parent1, parent2) for i in range(population_size)]
        children = [mutation_func(child) for child in children]
        # Reemplazo de la población anterior con la nueva población de hijos
        population = children
    # Obtención del mejor individuo de la última generación
    best_individual = min(population, key=fitness_func)
    return best_individual

# Ejemplo de uso del algoritmo genético para encontrar la ruta más corta entre dos nodos del grafo
start_node = 'A'
end_node = 'E'
best_route = genetic_algorithm(population_size=100, fitness_func=fitness, selection_func=selection, crossover_func=crossover, mutation_func=mutation, num_generations=100)
print('La ruta más corta desde {} hasta {} es: {}'.format(start_node, end_node, best_route))
