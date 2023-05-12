# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:55 2023

@author: carlo

Regla de la Cadena

En resumen, la Regla de la Cadena establece que la probabilidad conjunta de un 
conjunto de variables aleatorias puede descomponerse en el producto de las probabilidades 
condicionales de cada variable dada la información de las variables anteriores.
"""

# Definir las probabilidades individuales
P_fiebre = 0.2
P_dolor_cabeza = 0.3
P_gripe = 0.1

# Definir la probabilidad condicional
P_fiebre_dolor_cabeza_dada_gripe = 0.8

# Calcular la probabilidad conjunta
P_fiebre_dolor_cabeza_gripe = P_fiebre_dolor_cabeza_dada_gripe * P_gripe

# Calcular la probabilidad condicional
P_gripe_dada_fiebre_dolor_cabeza = P_fiebre_dolor_cabeza_gripe / (P_fiebre * P_dolor_cabeza)

print("La probabilidad de tener gripe dado que se tiene fiebre y dolor de cabeza es:", P_gripe_dada_fiebre_dolor_cabeza)
