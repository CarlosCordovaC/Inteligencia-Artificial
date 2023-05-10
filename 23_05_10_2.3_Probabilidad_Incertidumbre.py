# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:36:02 2023

@author: carlo

En resumen, la incertidumbre en probabilidad se refiere a la falta de conocimiento 
completo sobre los posibles resultados de un evento. En inteligencia artificial, se 
utilizan técnicas para cuantificar y gestionar esta incertidumbre, lo que permite 
tomar decisiones informadas y razonar de manera más robusta.
"""

from sklearn.datasets import load_sample_image
from sklearn.ensemble import RandomForestClassifier

# Cargar una muestra de imagen de gato
cat_image = load_sample_image("cat.jpg")

# Preparar los datos de entrenamiento y las etiquetas
X_train = [cat_image]
y_train = [1]  # 1 representa la clase de gato

# Crear y entrenar el clasificador
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Clasificar una imagen desconocida (por ejemplo, una imagen de perro)
unknown_image = load_sample_image("dog.jpg")
prediction = classifier.predict(unknown_image)

# Obtener las probabilidades de clasificación y la incertidumbre asociada
probabilities = classifier.predict_proba(unknown_image)
uncertainty = 1 - max(probabilities[0])  # La incertidumbre se calcula como 1 - la probabilidad máxima

# Imprimir los resultados
if prediction[0] == 1:
    print("La imagen es un gato")
else:
    print("La imagen es un perro")
print("Probabilidades de clasificación:", probabilities[0])
print("Incertidumbre:", uncertainty)


"""
Este ejemplo ilustra cómo podemos utilizar Python y una librería de aprendizaje 
automático para evaluar la incertidumbre en la clasificación de imágenes, lo que 
nos permite comprender mejor los resultados y tomar decisiones más adecuadas en 
función de la confianza del modelo.
"""