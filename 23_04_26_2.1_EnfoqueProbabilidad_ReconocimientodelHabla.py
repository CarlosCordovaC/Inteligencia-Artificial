# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:37:46 2023

@author: carlo

Un ejemplo cotidiano del reconocimiento del habla es el uso de asistentes de 
voz como Siri de Apple, Google Assistant y Amazon Alexa. Estos asistentes utilizan
 tecnología de reconocimiento del habla para comprender y responder a los comandos
 de voz de los usuarios. Por ejemplo, un usuario podría decir 
 "Hey Siri, ¿cuál es el clima de hoy?" y Siri respondería proporcionando la información
 meteorológica para el día.
 
 Reconocimiento del Habla
"""

import numpy as np

# Definición del modelo oculto de Markov
n_states = 3
n_obs = 4
n_time_steps = 5

# Probabilidades de transición entre estados
transition_probs = np.array([[0.4, 0.3, 0.3],
                             [0.2, 0.5, 0.3],
                             [0.1, 0.1, 0.8]])

# Probabilidades de emisión de cada estado para cada observación
emission_probs = np.array([[0.1, 0.3, 0.6, 0.0],
                           [0.3, 0.2, 0.1, 0.4],
                           [0.0, 0.1, 0.4, 0.5]])

# Probabilidades iniciales de cada estado
initial_probs = np.array([0.2, 0.4, 0.4])

# Generación de una secuencia de observaciones
obs_sequence = np.array([0, 1, 3, 2, 3])

# Forward algorithm para calcular la probabilidad de la secuencia observada
alpha = np.zeros((n_time_steps, n_states))
for i in range(n_time_steps):
    for j in range(n_states):
        if i == 0:
            alpha[i, j] = initial_probs[j] * emission_probs[j, obs_sequence[i]]
        else:
            alpha[i, j] = emission_probs[j, obs_sequence[i]] * np.sum(alpha[i-1, :] * transition_probs[:, j])

prob_obs_sequence = np.sum(alpha[-1, :])

print(f"La probabilidad de la secuencia observada {obs_sequence} es: {prob_obs_sequence}")
