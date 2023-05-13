# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:28:12 2023

@author: carlo

En resumen, el algoritmo EM es una técnica poderosa para estimar parámetros 
desconocidos en modelos probabilísticos cuando se tienen datos incompletos, y se 
basa en iteraciones entre los pasos de Expectation y Maximization para encontrar 
una estimación óptima.
"""

import numpy as np
from sklearn.mixture import GaussianMixture

# Datos de ejemplo
data = np.array([[1.5], [2.0], [4.2], [3.9], [7.1], [8.2]])

# Inicializar el modelo de mezcla gaussiana con dos componentes
model = GaussianMixture(n_components=2)

# Ajustar el modelo a los datos
model.fit(data)

# Obtener las etiquetas de los componentes
labels = model.predict(data)

# Imprimir las etiquetas asignadas a cada dato
for i in range(len(data)):
    print("Dato:", data[i][0], "Etiqueta:", labels[i])
