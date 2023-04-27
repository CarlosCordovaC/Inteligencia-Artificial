# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:41:46 2023

@author: carlo

Un ejemplo cotidiano de percepción es el reconocimiento de dígitos escritos a mano. 
Imagina que quieres desarrollar un programa que pueda leer números escritos a mano y 
reconocer qué número es. Primero, recopilas un conjunto de datos de entrenamiento que 
consiste en imágenes de números escritos a mano y sus correspondientes etiquetas. Cada 
imagen se convierte en una lista de características, como la intensidad de los píxeles 
en diferentes áreas de la imagen. Luego, se entrena un modelo de percepción con estos datos, 
de tal manera que pueda clasificar correctamente nuevas imágenes de números escritos a mano.

percepción
"""

import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=1, epochs=10):
        self.weights = np.zeros(input_size + 1)
        self.lr = lr
        self.epochs = epochs
    
    def activation_fn(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        z = self.weights.T.dot(x) + self.weights[0]
        a = self.activation_fn(z)
        return a
    
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(x)
                e = d[i] - y
                self.weights = self.weights + self.lr * e * x

# Datos de entrenamiento
X = np.array([[0,0], [0,1], [1,0], [1,1]])
d = np.array([0, 0, 0, 1])

# Creación de la percepción
perceptron = Perceptron(input_size=2)

# Entrenamiento
perceptron.fit(X, d)

# Predicción
for i in range(X.shape[0]):
    x = np.insert(X[i], 0, 1)
    y = perceptron.predict(x)
    print(f"Predicción para {X[i]}: {y}")

"""
En este ejemplo se está entrenando una Percepción para clasificar la operación lógica XOR. 
Se define la función de activación como la función escalón, y se utiliza el algoritmo de 
aprendizaje del descenso del gradiente para ajustar los pesos de la Percepción. 
La función predict() se utiliza para predecir la salida para una entrada dada.
"""
