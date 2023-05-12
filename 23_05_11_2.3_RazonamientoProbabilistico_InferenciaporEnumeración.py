# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:56 2023

@author: carlo

Inferencia por Enumeración

Este método es eficaz para modelos probabilísticos pequeños o con un número 
limitado de variables. Sin embargo, puede volverse computacionalmente costoso y 
poco práctico cuando se trabaja con modelos más grandes y complejos. En tales casos, 
se utilizan técnicas más avanzadas, como el muestreo de Monte Carlo y la propagación 
de creencias, para realizar inferencias probabilísticas de manera más eficiente.

"""

# Definir el modelo probabilístico
label_correct = 0.9
label_incorrect = 1 - label_correct

prob_fruit_given_correct = 0.6
prob_mint_given_correct = 0.4
prob_fruit_given_incorrect = 0.4
prob_mint_given_incorrect = 0.6

# Inferencia por enumeración
def enumeration_inference(observed_label):
    # Enumerar todas las combinaciones posibles
    combinations = [
        ('correct', 'fruit'),
        ('correct', 'mint'),
        ('incorrect', 'fruit'),
        ('incorrect', 'mint')
    ]

    # Calcular la probabilidad de cada combinación basada en las evidencias
    probabilities = []
    for combination in combinations:
        label, flavor = combination
        if observed_label == label:
            if flavor == 'fruit':
                probability = prob_fruit_given_correct if label == 'correct' else prob_fruit_given_incorrect
            else:
                probability = prob_mint_given_correct if label == 'correct' else prob_mint_given_incorrect
            probabilities.append(probability)
    
    # Normalizar las probabilidades
    total_probability = sum(probabilities)
    normalized_probabilities = [probability / total_probability for probability in probabilities]
    
    return normalized_probabilities

# Ejemplo de inferencia con etiqueta correcta
observed_label = 'correct'
result = enumeration_inference(observed_label)
print("Probabilidades de sabor a fruta y menta dado etiqueta correcta:", result)

# Ejemplo de inferencia con etiqueta incorrecta
observed_label = 'incorrect'
result = enumeration_inference(observed_label)
print("Probabilidades de sabor a fruta y menta dado etiqueta incorrecta:", result)

"""
Este ejemplo utiliza la función enumeration_inference para realizar la inferencia por
 enumeración. Simula el cálculo de las probabilidades de sabor a fruta y menta dado un
 etiquetado observado, ya sea correcto o incorrecto. Las probabilidades se calculan en
 base al modelo probabilístico definido y se normalizan para obtener resultados válidos.
"""