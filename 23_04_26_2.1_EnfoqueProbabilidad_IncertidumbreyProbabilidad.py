# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:57:11 2023

@author: carlo
"""

import random

def lanzar_dado():
    return random.randint(1, 6)

n = 1000
contador_unos = 0

for i in range(n):
    resultado = lanzar_dado()
    if resultado == 1:
        contador_unos += 1

probabilidad_uno = contador_unos / n

print("La probabilidad de sacar un 1 en un lanzamiento de dado es:", probabilidad_uno)
