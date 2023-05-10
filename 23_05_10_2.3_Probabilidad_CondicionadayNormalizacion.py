# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:45:42 2023

@author: carlo

En resumen, la probabilidad condicionada permite calcular probabilidades 
teniendo en cuenta información adicional, mientras que la normalización ajusta 
las probabilidades para que sumen 1 y sean comparables. Ambos conceptos son esenciales 
para el análisis y la modelización probabilística en la inteligencia artificial.
"""

# Datos de ejemplo
datos = [
    {'edad': 35, 'azucar': 120, 'diabetes': False},
    {'edad': 45, 'azucar': 150, 'diabetes': True},
    {'edad': 30, 'azucar': 100, 'diabetes': False},
    {'edad': 50, 'azucar': 200, 'diabetes': True},
    # ...
]

# Contar las ocurrencias de diabetes y nivel de azúcar por encima del umbral
ocurrencias_diabetes = 0
ocurrencias_azucar_alta = 0

for dato in datos:
    if dato['diabetes']:
        ocurrencias_diabetes += 1
        if dato['azucar'] > 140:
            ocurrencias_azucar_alta += 1
    elif dato['azucar'] > 140:
        ocurrencias_azucar_alta += 1

# Calcular la probabilidad condicionada
probabilidad_diabetes_dado_azucar_alta = ocurrencias_diabetes / ocurrencias_azucar_alta

# Normalizar las probabilidades
probabilidad_diabetes = ocurrencias_diabetes / len(datos)
probabilidad_azucar_alta = ocurrencias_azucar_alta / len(datos)

# Imprimir los resultados
print("Probabilidad de diabetes dado nivel de azúcar alto:", probabilidad_diabetes_dado_azucar_alta)
print("Probabilidad de diabetes:", probabilidad_diabetes)
print("Probabilidad de nivel de azúcar alto:", probabilidad_azucar_alta)
