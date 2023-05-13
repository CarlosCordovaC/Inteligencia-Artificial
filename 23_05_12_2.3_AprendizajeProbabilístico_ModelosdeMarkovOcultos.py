# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:37:31 2023

@author: carlo

Modelos de Markov Ocultos
En resumen, los Modelos de Markov Ocultos son herramientas poderosas en el campo de la 
inteligencia artificial para modelar y analizar secuencias de eventos o estados, 
especialmente cuando hay incertidumbre en la observación de esos eventos. Son utilizados 
en diversas aplicaciones, como reconocimiento de voz, procesamiento del lenguaje natural y 
reconocimiento de patrones.
"""

from hmmlearn import hmm
import numpy as np

# Definir el modelo de Markov oculto
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Entrenar el modelo con datos de ejemplo
X = np.array([[0.5], [1.2], [-0.3], [0.8], [1.1]])
model.fit(X)

# Predecir la secuencia más probable de estados ocultos
hidden_states = model.predict(X)

# Imprimir la secuencia de estados ocultos
print("Secuencia de estados ocultos:", hidden_states)


"""
En este ejemplo, estamos creando un modelo de Markov oculto con dos estados ocultos y 
una distribución de probabilidad gaussiana para cada estado. Luego, entrenamos el modelo 
con una secuencia de datos de ejemplo X y predecimos la secuencia más probable de estados 
ocultos para esos datos utilizando el método predict(). Finalmente, imprimimos la secuencia 
de estados ocultos resultante.
"""