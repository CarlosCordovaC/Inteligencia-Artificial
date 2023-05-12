# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:57 2023

@author: carlo

Monte Carlo para Cadenas de Markov

En resumen, el método de Monte Carlo para Cadenas de Markov consiste en generar una 
secuencia de muestras aleatorias a partir de una cadena de Markov, donde cada muestra 
depende únicamente de la muestra anterior. Estas muestras se utilizan para aproximar 
la distribución de probabilidad de interés.
"""

import random

# Probabilidades de transición observadas
transition_probabilities = {
    'soleado': {'soleado': 0.7, 'nublado': 0.2, 'lluvioso': 0.1},
    'nublado': {'soleado': 0.4, 'nublado': 0.4, 'lluvioso': 0.2},
    'lluvioso': {'soleado': 0.2, 'nublado': 0.3, 'lluvioso': 0.5}
}

def generate_weather_sequence(start_state, num_days):
    sequence = [start_state]

    for _ in range(num_days):
        current_state = sequence[-1]
        next_state = random.choices(
            population=list(transition_probabilities[current_state].keys()),
            weights=list(transition_probabilities[current_state].values())
        )[0]
        sequence.append(next_state)

    return sequence

# Generar una secuencia de clima para 1 día adicional comenzando desde 'soleado'
weather_sequence = generate_weather_sequence('soleado', 1)
print(weather_sequence)
