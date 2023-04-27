# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:59:25 2023

@author: carlo

Un ejemplo relacionado con la vida cotidiana podría ser la utilización de sistemas 
de recomendación en aplicaciones de música o películas. Estos sistemas utilizan modelos 
de Aprendizaje Profundo que utilizan técnicas de Aprendizaje Probabilístico para predecir 
las preferencias de los usuarios en función de su historial de escucha o visualización. 
 esta manera, pueden recomendar nuevos artistas o películas que puedan ser de interés para 
 el usuario.

Aprendizaje Profundo (Deep Learning)
"""

import numpy as np

# Funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    exps = np.exp(x)
    return exps / np.sum(exps)

# Datos de entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Arquitectura de la red
input_layer_size = 2
hidden_layer_size = 4
output_layer_size = 2

# Inicialización de los parámetros
W1 = np.random.randn(input_layer_size, hidden_layer_size)
b1 = np.zeros((1, hidden_layer_size))
W2 = np.random.randn(hidden_layer_size, output_layer_size)
b2 = np.zeros((1, output_layer_size))

# Hiperparámetros
learning_rate = 0.1
epochs = 10000

# Entrenamiento
for i in range(epochs):
    # Forward pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    y_hat = softmax(z2)

    # Cálculo del error
    loss = -np.log(y_hat[np.arange(len(y_hat)), y]).sum()

    # Backward pass
    delta3 = y_hat
    delta3[np.arange(len(y_hat)), y] -= 1
    dW2 = np.dot(a1.T, delta3)
    db2 = delta3.sum(axis=0, keepdims=True)
    delta2 = np.dot(delta3, W2.T) * sigmoid(z1) * (1 - sigmoid(z1))
    dW1 = np.dot(X.T, delta2)
    db1 = delta2.sum(axis=0)

    # Actualización de los parámetros
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Impresión del error cada 1000 epochs
    if i % 1000 == 0:
        print(f"Epoch {i}, Loss: {loss}")

# Predicción
z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, W2) + b2
y_hat = np.argmax(softmax(z2), axis=1)
print(f"Predicciones: {y_hat}")


"""
Este es un ejemplo de una red neuronal multicapa con una capa oculta de 4 neuronas, 
que utiliza la función de activación sigmoide en la capa oculta y la función softmax 
en la capa de salida para la clasificación de imágenes. El ejemplo utiliza la operación 
de producto punto de NumPy para la propagación hacia adelante y hacia atrás, y 
la actualización de los parámetros se realiza mediante la regla de actualización del 
gradiente descendente.
"""