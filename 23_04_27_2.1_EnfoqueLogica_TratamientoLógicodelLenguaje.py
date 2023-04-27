# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:00:23 2023

@author: carlo
Un ejemplo de aplicación del Tratamiento Lógico del Lenguaje es el sistema de 
asistencia virtual Siri de Apple. Siri es capaz de interpretar y responder preguntas 
en lenguaje natural utilizando técnicas de procesamiento de lenguaje natural y lógica. 
Por ejemplo, si le preguntas "¿Cuál es la temperatura en Nueva York hoy?", 
Siri procesará la pregunta utilizando técnicas de procesamiento de lenguaje natural 
para entender la pregunta y extraer la información relevante, y luego utilizará la 
lógica para buscar la respuesta en una base de datos de información meteorológica.

Tratamiento Lógico del Lenguaje
"""

import nltk
nltk.download('punkt')
# Definimos la lista de oraciones
oraciones = ["El perro juega en el parque.", 
             "El gato duerme en el sofá.", 
             "El pájaro canta en la ventana."]

# Tokenizamos cada oración
tokens = [nltk.word_tokenize(oracion) for oracion in oraciones]

# Creamos una función para buscar la palabra "perro"
def buscar_perro(tokens):
    for token in tokens:
        if token.lower() == 'perro':
            return True
    return False

# Buscamos la palabra "perro" en cada oración
for i, token in enumerate(tokens):
    if buscar_perro(token):
        print(f"La oración {i+1} contiene la palabra 'perro'")

"""
En este ejemplo, utilizamos la función word_tokenize de la biblioteca nltk para 
tokenizar cada una de las oraciones y convertirlas en una lista de palabras. Luego, 
creamos una función buscar_perro que busca la palabra "perro" en la lista de palabras. 
Por último, recorremos cada lista de palabras y llamamos a la función buscar_perro para 
buscar la palabra "perro". Si la palabra "perro" se encuentra en la lista de palabras, 
se imprime un mensaje indicando que la oración contiene la palabra "perro".
"""
