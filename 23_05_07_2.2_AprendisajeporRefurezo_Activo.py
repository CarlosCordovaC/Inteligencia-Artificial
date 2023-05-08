# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:05:35 2023

@author: carlo
En resumen, el aprendizaje por refuerzo activo implica que un agente aprenda a 
través de la interacción con su entorno, tomando decisiones y realizando acciones 
para maximizar las recompensas acumuladas. Utiliza estrategias de exploración y 
explotación para mejorar su conocimiento y aprendizaje a lo largo del tiempo.

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

# Definir los parámetros de aprendizaje
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 100

# Inicializar la tabla Q con ceros
q_table = np.zeros((4, 4))

# Algoritmo de Q-Learning
for episode in range(num_episodes):
    state = (3, 0)  # Estado inicial: posición del agente
    
    while True:
        # Elegir una acción basada en la política epsilon-greedy
        if np.random.uniform(0, 1) < 0.1:
            action = np.random.choice(actions)
        else:
            action = np.argmax(q_table[state])
        
        # Realizar la acción y obtener la siguiente posición y recompensa
        next_state = None
        reward = None
        
        if action == 0 and state[1] > 0 and env[state[0], state[1] - 1] != 1:
            next_state = (state[0], state[1] - 1)
            reward = -1 if env[next_state] == 2 else 0
        elif action == 1 and state[0] > 0 and env[state[0] - 1, state[1]] != 1:
            next_state = (state[0] - 1, state[1])
            reward = -1 if env[next_state] == 2 else 0
        elif action == 2 and state[1] < 3 and env[state[0], state[1] + 1] != 1:
            next_state = (state[0], state[1] + 1)
            reward = -1 if env[next_state] == 2 else 0
        elif action == 3 and state[0] < 3 and env[state[0] + 1, state[1]] != 1:
            next_state = (state[0] + 1, state[1])
            reward = -1 if env[next_state] == 2 else 0
        
        # Actualizar la tabla Q
        if next_state is not None and reward is not None:
            q_table[state][action] += learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[state][action])
        
        # Actualizar el estado actual
        state = next_state
        
        # Si el agente alcanza el objetivo, terminar el episodio
        if np.any(env[state] == 2):
            break


# Imprimir la tabla Q aprendida
print("Tabla Q aprendida:")
print(q_table)
