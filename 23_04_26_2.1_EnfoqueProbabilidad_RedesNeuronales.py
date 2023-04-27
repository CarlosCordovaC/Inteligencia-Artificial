# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:14:37 2023

@author: carlo

Un ejemplo de cómo se pueden aplicar las redes neuronales probabilísticas en la 
vida cotidiana es en la detección de spam en el correo electrónico. Un modelo de 
red neuronal probabilística puede aprender a clasificar correos electrónicos como 
spam o no spam en función de ciertas características, como la presencia de palabras 
clave, la dirección del remitente, el formato del correo electrónico, entre otras. 
En lugar de simplemente etiquetar un correo como spam o no spam, un modelo probabilístico 
puede calcular la probabilidad de que un correo sea spam o no, lo que permite tomar 
decisiones más informadas en la gestión del correo electrónico. Por ejemplo, se puede 
establecer un umbral de probabilidad por encima del cual los correos electrónicos se 
etiquetan como spam y se envían a una carpeta separada, mientras que los correos con 
una probabilidad menor se envían a la bandeja de entrada principal.

Redes Neuronales
"""


import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
from keras.datasets import mnist

# Cargar los datos
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocesamiento de los datos
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definición del modelo
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

# Compilación del modelo
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Entrenamiento del modelo
model.fit(X_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(X_test, y_test))

# Evaluación del modelo
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


"""
Este código es un ejemplo de una red neuronal que clasifica dígitos escritos a 
mano usando el conjunto de datos MNIST. La red neuronal está compuesta por dos capas: 
    una capa oculta con 512 neuronas y una capa de salida con 10 neuronas 
    (una para cada dígito). La función de activación de la capa oculta es ReLU, 
    mientras que la función de activación de la capa de salida es softmax. La función 
    de pérdida utilizada es categorical_crossentropy y el optimizador es Adam. 
    El modelo se entrena durante 10 épocas con un tamaño de lote de 128 y se evalúa en 
    el conjunto de datos de prueba.
"""