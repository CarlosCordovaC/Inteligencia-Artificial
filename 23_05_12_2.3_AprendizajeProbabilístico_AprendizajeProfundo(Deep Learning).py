# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:27:13 2023

@author: carlo

El aprendizaje profundo ha demostrado ser muy efectivo en una amplia gama de aplicaciones, 
como reconocimiento de imágenes, procesamiento del lenguaje natural, visión por computadora, 
traducción automática, conducción autónoma, entre otros. Su capacidad para aprender 
características y patrones complejos de manera automática lo convierte en una herramienta 
poderosa en el campo de la inteligencia artificial.

Aprendizaje Profundo (Deep Learning)
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar el conjunto de datos MNIST de dígitos escritos a mano
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizar las imágenes y convertirlas a vectores unidimensionales
X_train = X_train / 255.0
X_test = X_test / 255.0
X_train = X_train.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Definir el modelo de red neuronal profunda
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el rendimiento del modelo en el conjunto de pruebas
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Pérdida: {loss}")
print(f"Precisión: {accuracy}")
