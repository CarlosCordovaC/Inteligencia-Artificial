# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:18:06 2023

@author: carlo
En resumen, la exploración vs. explotación es un equilibrio crucial en el aprendizaje 
por refuerzo, donde el agente debe decidir entre aprovechar el conocimiento actual o 
explorar nuevas opciones para mejorar su rendimiento a largo plazo.
"""

import numpy as np

# Definir la configuración del entorno de bandit multi-brazo
num_brazos = 5
recompensas_verdaderas = np.random.normal(0, 1, num_brazos)

# Función para seleccionar una acción basada en la política epsilon-greedy
def seleccionar_accion(q_values, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        # Exploración: seleccionar una acción aleatoria
        return np.random.choice(len(q_values))
    else:
        # Explotación: seleccionar la acción con el valor Q más alto
        return np.argmax(q_values)

# Inicializar los valores Q y las cuentas de visitas para cada brazo
q_values = np.zeros(num_brazos)
visitas = np.zeros(num_brazos)

# Parámetros de aprendizaje
epsilon = 0.1
num_iteraciones = 1000

# Simulación del proceso de selección de acciones
for _ in range(num_iteraciones):
    accion = seleccionar_accion(q_values, epsilon)
    recompensa = np.random.normal(recompensas_verdaderas[accion], 1)
    
    # Actualizar el valor Q y la cuenta de visitas para la acción seleccionada
    visitas[accion] += 1
    q_values[accion] += (recompensa - q_values[accion]) / visitas[accion]

# Imprimir los valores Q aprendidos y las recompensas verdaderas
print("Valores Q aprendidos:", q_values)
print("Recompensas verdaderas:", recompensas_verdaderas)
