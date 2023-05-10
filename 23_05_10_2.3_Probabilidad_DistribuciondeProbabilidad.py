# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:51:49 2023

@author: carlo

En resumen, la distribución de probabilidad proporciona una descripción sistemática de 
las probabilidades asociadas con diferentes eventos o valores en un dominio. Proporciona 
una herramienta fundamental para comprender y modelar la incertidumbre en diversos problemas
 de inteligencia artificial, como el aprendizaje automático, la toma de decisiones y la 
 inferencia estadística. Ejemplos comunes de distribuciones de probabilidad incluyen la 
 distribución uniforme, la distribución normal (o gaussiana) y la distribución de Poisson.
"""


import numpy as np
import matplotlib.pyplot as plt

# Generar una distribución de probabilidad aleatoria
np.random.seed(0)
datos = np.random.normal(loc=5, scale=2, size=1000)

# Calcular la media y desviación estándar de los datos
media = np.mean(datos)
desviacion = np.std(datos)

# Generar una distribución de probabilidad normal utilizando los parámetros calculados
distribucion = np.random.normal(loc=media, scale=desviacion, size=10000)

# Visualizar la distribución de probabilidad generada
plt.hist(distribucion, bins=30, density=True)
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad Normal')
plt.show()
