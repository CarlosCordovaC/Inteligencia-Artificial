# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:05 2023

@author: carlo

Ponderación de Verosimilitud

En resumen, la ponderación de verosimilitud implica asignar un peso a cada observación 
o dato según su credibilidad o confiabilidad, y utilizar estos pesos para actualizar 
las probabilidades iniciales y obtener estimaciones más precisas.

"""

import random

def generar_lanzamiento():
    return random.choice(['cara', 'sello'])

def generar_datos(num_lanzamientos):
    datos = []
    for _ in range(num_lanzamientos):
        datos.append(generar_lanzamiento())
    return datos

# Generar datos observados (10 lanzamientos)
datos_observados = generar_datos(10)

# Probabilidad inicial de que la moneda sea justa
probabilidad_justa = 0.5

# Ponderación de verosimilitud
pesos = []
for dato in datos_observados:
    if dato == 'cara':
        peso = probabilidad_justa
    else:
        peso = 1 - probabilidad_justa
    pesos.append(peso)

# Actualizar la probabilidad basada en la ponderación de verosimilitud
suma_pesos = sum(pesos)
probabilidad_justa_actualizada = sum(pesos) / len(datos_observados)

print("Probabilidad inicial de que la moneda sea justa:", probabilidad_justa)
print("Probabilidad actualizada de que la moneda sea justa:", probabilidad_justa_actualizada)
