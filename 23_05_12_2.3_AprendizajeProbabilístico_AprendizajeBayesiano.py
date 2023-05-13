# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:13:49 2023

@author: carlo

En resumen, el Aprendizaje Bayesiano en Inteligencia Artificial utiliza el razonamiento
 probabilístico y el Teorema de Bayes para actualizar creencias, realizar inferencias y 
 tomar decisiones basadas en la evidencia observada. Este enfoque tiene aplicaciones en 
 la clasificación, estimación de parámetros, inferencia de redes y otros problemas 
 relacionados con el aprendizaje automático y la inteligencia artificial.
 
 P(Lluvia) = (P(Pronóstico|Lluvia) * P(Lluvia)) / (P(Pronóstico|Lluvia) * P(Lluvia) + P(Pronóstico|No Lluvia) * P(No Lluvia))
"""

import numpy as np

# Datos de entrenamiento
# Matriz de características: [Presencia de "oferta", Longitud]
X = np.array([[1, 20], [0, 15], [1, 30], [0, 25]])
# Etiquetas de clase: 1 para spam, 0 para no spam
y = np.array([1, 0, 1, 0])

# Función para calcular las probabilidades a priori
def calcular_probabilidades_priori(y):
    clases, counts = np.unique(y, return_counts=True)
    total = len(y)
    probabilidades = {}
    for clase, count in zip(clases, counts):
        probabilidades[clase] = count / total
    return probabilidades

# Función para calcular las probabilidades condicionales
def calcular_probabilidades_condicionales(X, y):
    clases = np.unique(y)
    probabilidades = {}
    for clase in clases:
        X_clase = X[y == clase]
        num_muestras_clase = len(X_clase)
        probabilidades[clase] = {}
        for feature in range(X.shape[1]):
            valores, counts = np.unique(X_clase[:, feature], return_counts=True)
            prob_feature = {}
            for valor, count in zip(valores, counts):
                prob_feature[valor] = count / num_muestras_clase
            probabilidades[clase][feature] = prob_feature
    return probabilidades

# Función para predecir la clase de un nuevo ejemplo
def predecir(clases, probabilidades_priori, probabilidades_condicionales, ejemplo):
    mejor_clase = None
    mejor_probabilidad = -1
    for clase in clases:
        probabilidad = probabilidades_priori[clase]
        for feature, valor in enumerate(ejemplo):
            if valor in probabilidades_condicionales[clase][feature]:
                probabilidad *= probabilidades_condicionales[clase][feature][valor]
        if probabilidad > mejor_probabilidad:
            mejor_clase = clase
            mejor_probabilidad = probabilidad
    return mejor_clase

# Calcular las probabilidades a priori y condicionales
probabilidades_priori = calcular_probabilidades_priori(y)
probabilidades_condicionales = calcular_probabilidades_condicionales(X, y)

# Ejemplo de prueba
ejemplo_prueba = [1, 18]
clases = np.unique(y)
clase_predicha = predecir(clases, probabilidades_priori, probabilidades_condicionales, ejemplo_prueba)

print("La clase predicha para el ejemplo de prueba [1, 18] es:", clase_predicha)


"""
En este ejemplo, se utilizan las probabilidades a priori y condicionales para predecir 
la clase (spam o no spam) de un nuevo ejemplo de correo electrónico basado en la presencia 
de la palabra "oferta" y la longitud del correo electrónico. Las probabilidades a priori 
se calculan en función de la proporción de ejemplos en cada clase, mientras que las 
probabilidades condicionales se calculan en función de la proporción de ejemplos con 
ciertos valores de características en cada clase.
"""