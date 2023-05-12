# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:03 2023

@author: carlo

Red Bayes. Dinámica: Filtrado de Partículas
"""

import numpy as np
import matplotlib.pyplot as plt

# Función para simular la dinámica del sistema
def simular_dinamica(x, u):
    A = np.array([[1, 1],
                  [0, 1]])
    B = np.array([[0.5, 0],
                  [1, 0]])
    w = np.random.normal(0, 0.1, size=(2,))
    return A.dot(x) + B.dot(u) + w

# Función para simular las mediciones ruidosas
def simular_medicion(x):
    H = np.array([[1, 0]])
    v = np.random.normal(0, 0.1)
    return H.dot(x) + v

# Función para calcular la ponderación de las partículas
def calcular_ponderaciones(particulas, medicion):
    diferencias = particulas - medicion
    distancias_cuad = np.sum(diferencias**2, axis=1)
    ponderaciones = np.exp(-distancias_cuad / (2 * 0.1**2))
    return ponderaciones / np.sum(ponderaciones)

# Parámetros del filtro de partículas
num_particulas = 100
x_true = np.array([0, 0])
u = np.array([1, 0.5])

# Generar las partículas iniciales
particulas = np.random.normal(0, 1, size=(num_particulas, 2))

# Simular el filtro de partículas
num_pasos = 50
x_estimado = np.zeros((num_pasos, 2))

for t in range(num_pasos):
    # Simular la dinámica del sistema
    x_true = simular_dinamica(x_true, u)

    # Simular las mediciones ruidosas
    z = simular_medicion(x_true)

    # Actualizar las ponderaciones de las partículas
    ponderaciones = calcular_ponderaciones(particulas, z)

    # Muestrear nuevas partículas basadas en las ponderaciones
    indices = np.random.choice(range(num_particulas), size=num_particulas, replace=True, p=ponderaciones)
    particulas = particulas[indices]

    # Estimar el estado utilizando el promedio de las partículas
    x_estimado[t] = np.mean(particulas, axis=0)

# Graficar los resultados
plt.figure()
plt.plot(x_true[:, 0], x_true[:, 1], label='Posición verdadera')
plt.scatter(x_estimado[:, 0], x_estimado[:, 1], color='red', label='Estimación')
plt.xlabel('Posición X')
plt.ylabel('Velocidad')
plt.legend()
plt.title('Filtrado de Partículas')
plt.show()
