# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:05 2023

@author: carlo

Procesos Estacionarios

Los Procesos Estacionarios son utilizados en la inteligencia artificial para modelar y 
predecir fenómenos que exhiben cierta estabilidad estadística a lo largo del tiempo. 
Algunos ejemplos comunes incluyen la predicción de series temporales, análisis de señales 
y modelado de datos de sensores.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del proceso AR(1)
phi = 0.8  # Coeficiente de autoregresión
mu = 0  # Media
sigma = 1  # Desviación estándar

# Generar una serie de tiempo estacionaria
n = 100  # Número de puntos en la serie
x = np.zeros(n)
x[0] = np.random.normal(mu, sigma)  # Valor inicial aleatorio

for t in range(1, n):
    x[t] = phi * x[t-1] + np.random.normal(mu, sigma)

# Graficar la serie de tiempo
plt.plot(x)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Proceso AR(1) Estacionario')
plt.show()
