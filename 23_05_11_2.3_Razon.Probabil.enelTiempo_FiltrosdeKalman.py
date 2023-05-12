# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:03 2023

@author: carlo
Filtros de Kalman
"""

import numpy as np

# Función para simular la posición verdadera del objeto
def simular_posicion_verdadera(velocidad, dt):
    A = np.array([[1, dt],
                  [0, 1]])
    x = np.array([[0],
                  [0]])
    B = np.array([[0.5 * dt**2],
                  [dt]])
    u = np.array([[0.1]])
    return A.dot(x) + B.dot(u)

# Función para simular la medición ruidosa de la posición del objeto
def simular_medicion(posicion_verdadera, ruido_medicion):
    H = np.array([[1, 0]])
    v = np.random.normal(0, ruido_medicion)
    return H.dot(posicion_verdadera) + v

# Parámetros del filtro de Kalman
A = np.array([[1, 1],
              [0, 1]])
H = np.array([[1, 0]])
Q = np.array([[0.001, 0],
              [0, 0.001]])
R = np.array([[0.1]])

# Estado inicial
x = np.array([[0],
              [0]])

# Matriz de covarianza inicial
P = np.array([[1, 0],
              [0, 1]])

# Simulación del seguimiento del objeto
velocidad_objeto = 1
ruido_medicion = 0.5
num_pasos = 100

posiciones_verdaderas = []
mediciones = []
estimaciones = []

for t in range(num_pasos):
    # Simular la posición verdadera del objeto
    posicion_verdadera = simular_posicion_verdadera(velocidad_objeto, dt=1)

    # Simular la medición ruidosa de la posición del objeto
    medicion = simular_medicion(posicion_verdadera, ruido_medicion)

    # Actualizar el estado y la matriz de covarianza utilizando el filtro de Kalman
    # Paso de predicción
    x_prediccion = A.dot(x)
    P_prediccion = A.dot(P).dot(A.T) + Q

    # Paso de corrección
    innovacion = medicion - H.dot(x_prediccion)
    S = H.dot(P_prediccion).dot(H.T) + R
    K = P_prediccion.dot(H.T).dot(np.linalg.inv(S))
    x = x_prediccion + K.dot(innovacion)
    P = (np.eye(2) - K.dot(H)).dot(P_prediccion)

    # Almacenar las posiciones verdaderas, mediciones y estimaciones
    posiciones_verdaderas.append(posicion_verdadera[0, 0])
    mediciones.append(medicion[0, 0])
    estimaciones.append(x[0, 0])

# Imprimir las posiciones verdaderas, mediciones y estimaciones
print("Posiciones verdaderas:", posiciones_verdaderas)
print("Mediciones:", mediciones)
print("Estimaciones del filtro de Kalman:", estimaciones)
