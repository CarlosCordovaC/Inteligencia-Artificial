# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:38:54 2023

@author: carlo
En resumen, la probabilidad a priori es una estimación inicial de la probabilidad de un 
evento o hipótesis antes de tener datos o evidencia observados. En el contexto de la 
inteligencia artificial, esta probabilidad inicial puede influir en la toma de decisiones 
y en la asignación de probabilidades a eventos futuros en función de la información previa.
"""

import numpy as np

# Datos de ejemplo (clases etiquetadas)
data = np.array([[3, 1, 2],
                 [2, 2, 1],
                 [1, 3, 1],
                 [2, 1, 2],
                 [1, 2, 2]])

# Índices de clase en los datos
class_labels = np.array([1, 1, 2, 2, 3])

# Calcular la probabilidad a priori de cada clase
total_samples = len(class_labels)
unique_classes = np.unique(class_labels)
prior_probabilities = []

for cls in unique_classes:
    class_count = np.sum(class_labels == cls)
    prior_prob = class_count / total_samples
    prior_probabilities.append(prior_prob)

# Imprimir los resultados
for i, cls in enumerate(unique_classes):
    print("Probabilidad a priori de la clase {}: {:.2f}".format(cls, prior_probabilities[i]))


"""
En este ejemplo, tenemos un conjunto de datos data con características (atributos) y 
etiquetas de clase class_labels. Calculamos la probabilidad a priori de cada clase al 
contar la cantidad de instancias en cada clase y dividirla por el número total de 
instancias.

El resultado mostrará las probabilidades a priori para cada clase en el conjunto de datos. 
Por ejemplo, si tenemos 5 instancias en total y 2 pertenecen a la clase 1, la probabilidad 
a priori de la clase 1 sería 2/5 = 0.4.
"""
