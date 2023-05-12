# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:04 2023

@author: carlo

Hipótesis de Markov: Procesos de Markov

La Hipótesis de Markov, también conocida como propiedad de Markov, es un concepto 
fundamental en el campo de los procesos estocásticos, especialmente en los Procesos 
de Markov. Esta hipótesis establece que la probabilidad de que un evento futuro ocurra 
depende únicamente del estado presente y no de los estados anteriores.

"""

import numpy as np

# Definir la matriz de transición
transition_matrix = np.array([[0.7, 0.3],
                              [0.2, 0.8]])

# Definir los estados posibles
states = ['Soleado', 'Lluvioso']

# Definir el estado inicial
initial_state = 'Soleado'

# Generar una secuencia de estados basada en el proceso de Markov
sequence_length = 10
current_state = initial_state
state_sequence = [current_state]

for _ in range(sequence_length - 1):
    next_state = np.random.choice(states, p=transition_matrix[states.index(current_state)])
    state_sequence.append(next_state)
    current_state = next_state

# Imprimir la secuencia de estados generada
print(state_sequence)


"""
En este ejemplo, se define una matriz de transición que representa la probabilidad de 
pasar de un estado a otro. En este caso, los estados posibles son "Soleado" y "Lluvioso". 
El código genera una secuencia de estados basada en el proceso de Markov, donde en cada 
paso se selecciona el siguiente estado de acuerdo con las probabilidades de transición.
"""