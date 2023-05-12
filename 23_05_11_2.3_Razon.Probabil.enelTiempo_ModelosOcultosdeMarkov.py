# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:04 2023

@author: carlo

Modelos Ocultos de Markov
"""
from hmmlearn import hmm

# Definir los estados ocultos
estados_ocultos = ["soleado", "nublado", "lluvioso"]

# Definir las observaciones
observaciones = ["caminar", "comer", "dormir"]

# Crear el modelo HMM
modelo = hmm.MultinomialHMM(n_components=len(estados_ocultos))

# Definir las probabilidades de transición
prob_transicion = [[0.7, 0.2, 0.1],
                   [0.3, 0.5, 0.2],
                   [0.2, 0.3, 0.5]]

# Definir las probabilidades de emisión
prob_emision = [[0.6, 0.3, 0.1],
                [0.1, 0.6, 0.3],
                [0.3, 0.1, 0.6]]

# Establecer las probabilidades de transición y emisión en el modelo
modelo.startprob_ = [0.4, 0.3, 0.3]
modelo.transmat_ = prob_transicion
modelo.emissionprob_ = prob_emision

# Generar una secuencia de observaciones usando el modelo HMM
secuencia_observaciones, secuencia_estados_ocultos = modelo.sample(10)

# Imprimir la secuencia generada
print("Secuencia de observaciones generada:", secuencia_observaciones)
print("Secuencia de estados ocultos generada:", [estados_ocultos[i] for i in secuencia_estados_ocultos])
