# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:43:13 2023

@author: carlo
Un ejemplo de la vida diaria podría ser el siguiente: supongamos que estás pensando en 
comprar un automóvil y tienes varias opciones en mente. Antes de tomar una decisión, 
puedes evaluar el valor de obtener información adicional sobre el rendimiento del 
combustible, el historial de mantenimiento y la seguridad de cada automóvil. 
Si determinas que esta información adicional te permitiría tomar una decisión más 
informada y potencialmente afectaría tus preferencias y utilidad esperada, entonces 
el valor de adquirir esa información sería alto. Esto te ayudaría a tomar una decisión 
más fundamentada y a seleccionar el automóvil que mejor se ajuste a tus necesidades y 
preferencias.
"""

import random

def valor_informacion(probabilidades, utilidades):
    valor_informacion = 0
    for i in range(len(probabilidades)):
        valor_informacion += probabilidades[i] * utilidades[i]
    return valor_informacion

def tomar_decision(probabilidades, utilidades):
    mejor_decision = None
    mejor_valor_informacion = float('-inf')
    
    for i in range(len(probabilidades)):
        decision_actual = i
        probabilidades_actualizadas = probabilidades[:]
        probabilidades_actualizadas[i] = random.uniform(0, 1)  # Simulación de nueva información
        valor_informacion_actual = valor_informacion(probabilidades_actualizadas, utilidades)
        
        if valor_informacion_actual > mejor_valor_informacion:
            mejor_valor_informacion = valor_informacion_actual
            mejor_decision = decision_actual
    
    return mejor_decision

# Ejemplo de toma de decisiones de inversión
probabilidades = [0.4, 0.6, 0.8]  # Probabilidades de éxito para cada decisión
utilidades = [1000, 2000, 3000]  # Utilidades esperadas para cada decisión

mejor_decision = tomar_decision(probabilidades, utilidades)
print("Mejor decisión:", mejor_decision)


"""
En este ejemplo, se considera una situación en la que se deben tomar 
decisiones de inversión. Cada decisión tiene una probabilidad asociada de éxito 
y una utilidad esperada en caso de éxito. La función tomar_decision simula la 
adquisición de nueva información modificando las probabilidades de éxito de manera 
aleatoria. Luego, se calcula el valor de la información para cada decisión y se 
selecciona la decisión con el mayor valor de información como la mejor opción.


"""