# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:25:52 2023

@author: carlo

El Naïve-Bayes es rápido y eficiente, ya que solo requiere estimar las probabilidades a 
priori y condicionales a partir de los datos de entrenamiento. Sin embargo, la suposición 
de independencia puede no ser válida en algunos casos, lo que puede afectar la precisión 
del modelo. A pesar de esta limitación, el Naïve-Bayes sigue siendo un algoritmo popular 
y ampliamente utilizado en muchas aplicaciones de clasificación.
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Datos de entrenamiento
correos = [
    'Gana dinero rápido y fácil con nuestras ofertas especiales',
    'Reunión de proyecto el próximo martes',
    'Confirma tu asistencia a la fiesta de fin de año',
    'Amplía tus habilidades con nuestros cursos en línea'
]
etiquetas = ['spam', 'no spam', 'no spam', 'no spam']

# Preprocesamiento de los datos de texto
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(correos)

# Entrenamiento del modelo Naïve-Bayes
model = MultinomialNB()
model.fit(X_train, etiquetas)

# Datos de prueba
nuevo_correo = ['Gana dinero con nuestras increíbles promociones']

# Preprocesamiento del nuevo correo
X_test = vectorizer.transform(nuevo_correo)

# Clasificación del nuevo correo
prediccion = model.predict(X_test)

# Resultado
print('La clasificación del correo es:', prediccion)


"""
En este ejemplo, se utiliza el algoritmo Naïve-Bayes multinomial de la biblioteca 
scikit-learn para clasificar correos electrónicos como spam o no spam. Se utiliza el 
conteo de palabras (CountVectorizer) para convertir los textos en características 
numéricas que el modelo puede entender.

Primero, se entrenan los datos utilizando los correos electrónicos de entrenamiento y 
sus etiquetas correspondientes. Luego, se prepara un nuevo correo electrónico de prueba 
y se transforma utilizando el mismo vectorizador de palabras. Finalmente, se realiza la 
clasificación del nuevo correo y se muestra el resultado.
"""