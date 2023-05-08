# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:20:59 2023

@author: carlo

En resumen, la Búsqueda de la Política es una técnica que busca la mejor estrategia o 
conjunto de reglas para tomar decisiones en un problema, explorando diferentes políticas 
y evaluando su desempeño. Es una forma de encontrar la mejor política de toma de decisiones 
en un problema sin necesariamente utilizar métodos de aprendizaje o estimación de valores.
"""

import numpy as np

# Definir el entorno (laberinto)
# 0: espacio vacío
# 1: pared
# 2: objetivo (salida)
# 3: agente
env = np.array([
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 2]
])

# Definir los posibles movimientos
# 0: izquierda
# 1: arriba
# 2: derecha
# 3: abajo
actions = [0, 1, 2, 3]

# Definir una política inicial aleatoria
policy = np.random.choice(actions, size=(4, 4))

# Función para evaluar una política
def evaluate_policy(policy):
    state = (3, 0)  # Estado inicial: posición del agente
    path = [state]

    while True:
        action = policy[state]
        
        # Realizar la acción y obtener la siguiente posición
        next_state = None
        
        if action == 0 and state[1] > 0 and env[state[0], state[1] - 1] != 1:
            next_state = (state[0], state[1] - 1)
        elif action == 1 and state[0] > 0 and env[state[0] - 1, state[1]] != 1:
            next_state = (state[0] - 1, state[1])
        elif action == 2 and state[1] < 3 and env[state[0], state[1] + 1] != 1:
            next_state = (state[0], state[1] + 1)
        elif action == 3 and state[0] < 3 and env[state[0] + 1, state[1]] != 1:
            next_state = (state[0] + 1, state[1])
        
        # Actualizar el estado actual
        state = next_state
        path.append(state)
        
        # Si el agente alcanza el objetivo, terminar la evaluación
        if np.any(env[state] == 2):
            break

    return path

# Ejecutar la búsqueda de la política
num_iterations = 10
for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}:")
    print("Policy:")
    print(policy)
    
    # Evaluar la política actual
    path = evaluate_policy(policy)
    print("Path:")
    for state in path:
        print(state)
    
    # Actualizar la política basada en el resultado de la evaluación
    policy = np.random.choice(actions, size=(4, 4))

print("Final Policy:")
print(policy)


"""
En este ejemplo, se define un laberinto representado como una matriz, y se define una 
política inicial aleatoria. Luego, se utiliza la función evaluate_policy para evaluar 
la política actual, es decir, se simula el recorrido del agente siguiendo la política 
y se registra el camino que toma. Después de evaluar la política, se actualiza la política 
de forma aleatoria y se repite el proceso varias veces.
"""