# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:56 2023

@author: carlo

Manto de Markov

En resumen, el Manto de Markov implica que, dada la información del estado actual, 
no es necesario tener conocimiento sobre los estados pasados para predecir el estado 
futuro. Esto hace que el modelado y el análisis de sistemas sean más eficientes y manejables, 
especialmente en situaciones donde el historial completo de estados es difícil de obtener 
o no es relevante.
"""

import random

# Definir la matriz de transición del clima
transition_matrix = {
    'soleado': {'soleado': 0.8, 'nublado': 0.1, 'lluvioso': 0.1},
    'nublado': {'soleado': 0.3, 'nublado': 0.4, 'lluvioso': 0.3},
    'lluvioso': {'soleado': 0.2, 'nublado': 0.4, 'lluvioso': 0.4}
}

# Función para predecir el clima futuro
def predecir_clima(dia_actual, num_dias):
    clima_actual = dia_actual
    print("Día 1:", clima_actual)
    
    for dia in range(2, num_dias + 1):
        clima_siguiente = random.choices(
            list(transition_matrix[clima_actual].keys()),
            list(transition_matrix[clima_actual].values())
        )[0]
        print("Día", dia, ":", clima_siguiente)
        clima_actual = clima_siguiente

# Predecir el clima para los próximos 5 días
predecir_clima('soleado', 5)
