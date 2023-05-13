# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:51:29 2023

@author: carlo
Máquinas de Vectores Soporte (Núcleo)

En resumen, las SVM utilizan un enfoque basado en el concepto de hiperplanos y los 
vectores de soporte para realizar clasificaciones precisas en espacios de alta dimensión. 
Además, el uso de núcleos permite manejar datos que no son linealmente separables en su 
forma original. Las SVM han demostrado ser eficaces en una amplia gama de aplicaciones, 
como reconocimiento de imágenes, clasificación de texto y detección de anomalías.

"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()

# Dividir los datos en características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo SVM
svm_model = SVC(kernel='linear')

# Entrenar el modelo con el conjunto de entrenamiento
svm_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = svm_model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
