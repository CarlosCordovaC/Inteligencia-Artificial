# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:04 2023

@author: carlo

Algoritmo Hacia Delante-Atrás

En resumen, el algoritmo hacia adelante-atrás es una técnica fundamental para estimar 
los parámetros ocultos en un modelo de Markov oculto, lo que permite realizar tareas de 
aprendizaje no supervisado y estimación de estados ocultos en inteligencia artificial.
"""
import numpy as np

# Secuencia de observaciones
observaciones = np.array(['soleado', 'nublado', 'lluvioso', 'soleado', 'nublado'])


# Estados ocultos
estados_ocultos = ['soleado', 'nublado', 'lluvioso']

# Probabilidades de transición iniciales
prob_transicion = np.array([[0.4, 0.3, 0.3],
                            [0.2, 0.5, 0.3],
                            [0.1, 0.2, 0.7]])

# Probabilidades de observación iniciales
prob_observacion = np.array([[0.6, 0.3, 0.1],
                             [0.1, 0.7, 0.2],
                             [0.2, 0.4, 0.4]])

# Algoritmo hacia adelante
def forward_algorithm(obs, trans, obs_prob):
    T = len(obs)
    N = trans.shape[0]
    alpha = np.zeros((T, N))

    # Inicializar alpha con la probabilidad inicial
    alpha[0] = obs_prob[:, obs[0]]

    # Calcular las probabilidades hacia adelante recursivamente
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = np.sum(alpha[t-1] * trans[:, j]) * obs_prob[j, obs[t]]

    return alpha

# Algoritmo hacia atrás
def backward_algorithm(obs, trans, obs_prob):
    T = len(obs)
    N = trans.shape[0]
    beta = np.zeros((T, N))

    # Inicializar beta con 1 para el último día
    beta[T-1] = 1

    # Calcular las probabilidades hacia atrás recursivamente
    for t in range(T-2, -1, -1):
        for i in range(N):
            beta[t, i] = np.sum(beta[t+1] * trans[i, :] * obs_prob[:, obs[t+1]])

    return beta

# Estimación de los parámetros ocultos
def estimate_parameters(obs, trans, obs_prob):
    alpha = forward_algorithm(obs, trans, obs_prob)
    beta = backward_algorithm(obs, trans, obs_prob)

    T = len(obs)
    N = trans.shape[0]
    gamma = alpha * beta / np.sum(alpha * beta, axis=1).reshape(-1, 1)

    xi = np.zeros((T-1, N, N))
    for t in range(T-1):
        for i in range(N):
            for j in range(N):
                xi[t, i, j] = alpha[t, i] * trans[i, j] * obs_prob[j, obs[t+1]] * beta[t+1, j]
        xi[t] /= np.sum(xi[t])

    # Actualizar las probabilidades de transición y observación
    new_trans = np.sum(xi, axis=0) / np.sum(gamma[:-1], axis=0).reshape(-1, 1)
    new_obs_prob = np.copy(obs_prob)
    for k in range(N):
        for l in range(len(set(obs))):
            mask = obs == l
            new_obs_prob[k, l] = np.sum(gamma[mask, k]) / np.sum(gamma[mask])

    return new_trans, new_obs_prob

# Estimar los parámetros ocultos
new_trans, new_obs_prob = estimate_parameters(observaciones, prob_transicion, prob_observacion)

print("Probabilidades de transición actualizadas:")
print(new_trans)
print("\nProbabilidades de observación actualizadas:")
print(new_obs_prob)

