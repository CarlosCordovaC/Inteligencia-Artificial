# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:24:04 2023

@author: carlo

Un ejemplo práctico del TPL en la vida cotidiana es el sistema de corrección 
ortográfica de los teléfonos móviles. Este sistema utiliza modelos probabilísticos 
para predecir la palabra correcta a medida que el usuario escribe. Por ejemplo, si el 
usuario escribe "hol", el sistema puede sugerir "hola" en lugar de "holgazán" 
porque "hola" es más probable en ese contexto.

Tratamiento Probabilístico del Lenguaje(TPL)

"""

import random

# Ejemplo de datos de entrenamiento
corpus = "El gato come pescado. La gata come ratón. El perro ladra al gato."

# Función para generar pares de palabras
def generate_word_pairs(corpus):
    words = corpus.split()
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

# Crear tabla de transición de probabilidad
def create_transition_table(corpus):
    pairs = list(generate_word_pairs(corpus))
    table = {}
    for pair in pairs:
        if pair[0] not in table:
            table[pair[0]] = {}
        if pair[1] not in table[pair[0]]:
            table[pair[0]][pair[1]] = 0
        table[pair[0]][pair[1]] += 1
    for word in table:
        total_count = sum(table[word].values())
        for next_word in table[word]:
            table[word][next_word] /= total_count
    return table

# Generar una oración aleatoria usando la tabla de transición
def generate_sentence(transition_table):
    current_word = random.choice(list(transition_table.keys()))
    sentence = [current_word]
    while True:
        if current_word not in transition_table:
            break
        next_word_probs = transition_table[current_word]
        if not next_word_probs:
            break
        next_word = max(next_word_probs, key=lambda x: next_word_probs[x])
        sentence.append(next_word)
        current_word = next_word
    return " ".join(sentence)

# Entrenar el modelo y generar una oración aleatoria
transition_table = create_transition_table(corpus)
print(generate_sentence(transition_table))


"""
Este código genera una tabla de transición de probabilidad a partir de una cadena de 
texto y luego genera una oración aleatoria utilizando esta tabla. El modelo de lenguaje 
probabilístico utiliza una cadena de Markov de orden uno, lo que significa que la 
probabilidad de cada palabra depende solo de la palabra inmediatamente anterior. 
Este enfoque es útil para generar texto con cierto grado de coherencia y cohesión, 
 no es adecuado para tareas más complejas, como la traducción automática o el reconocimiento 
 de voz.
"""