# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:08:44 2023

@author: carlo

Un ejemplo práctico de esta técnica se podría aplicar en la organización de un armario. 
Imagina que tienes un armario con muchas prendas de ropa y quieres organizarlo de manera 
eficiente. Si aplicas la técnica de búsqueda local, podrías comenzar por colocar las prendas 
de ropa en lugares aleatorios del armario y luego ir moviendo las prendas para que se cumplan 
las restricciones (por ejemplo, no poner una camisa sobre otra). En lugar de tratar de 
encontrar la solución perfecta de inmediato, esta técnica se enfocaría en mejorar la 
organización del armario con el tiempo.

Búsqueda Local: Mínimos-Conflictos
"""

import random

# Definir el mapa y sus restricciones
mapa = {
    "A": ["B", "D"],
    "B": ["A", "C", "D"],
    "C": ["B", "D", "E"],
    "D": ["A", "B", "C", "E"],
    "E": ["C", "D"]
}

colores_disponibles = ["rojo", "verde", "azul", "amarillo"]

restricciones = {
    "A": ["B", "D"],
    "B": ["A", "C", "D"],
    "C": ["B", "D", "E"],
    "D": ["A", "B", "C", "E"],
    "E": ["C", "D"]
}

# Asignar colores aleatorios a cada país
asignacion = {}
for pais in mapa:
    asignacion[pais] = random.choice(colores_disponibles)

# Función para evaluar la calidad de la asignación
def evaluar(asignacion):
    conflictos = 0
    for pais in mapa:
        for vecino in mapa[pais]:
            if asignacion[pais] == asignacion[vecino]:
                conflictos += 1
    return conflictos

# Función para resolver el problema usando búsqueda local de mínimos conflictos
def resolver():
    # Iterar hasta encontrar una solución o hasta llegar a un número máximo de iteraciones
    max_iteraciones = 1000
    for i in range(max_iteraciones):
        conflictos = evaluar(asignacion)
        if conflictos == 0:
            # Solución encontrada, devolver la asignación
            return asignacion
        
        # Encontrar un país con conflictos y asignarle un color que minimice los conflictos
        paises_con_conflictos = [pais for pais in mapa if any(asignacion[pais] == asignacion[vecino] for vecino in mapa[pais])]
        pais_a_cambiar = random.choice(paises_con_conflictos)
        mejores_colores = []
        for color in colores_disponibles:
            asignacion[pais_a_cambiar] = color
            conflictos_nuevos = evaluar(asignacion)
            if conflictos_nuevos < conflictos:
                mejores_colores = [color]
                conflictos = conflictos_nuevos
            elif conflictos_nuevos == conflictos:
                mejores_colores.append(color)
        asignacion[pais_a_cambiar] = random.choice(mejores_colores)
    
    # Si llegamos aquí, no se encontró solución después de las iteraciones máximas
    return None

# Ejemplo de uso
asignacion = resolver()
if asignacion is not None:
    print("Solución encontrada:")
    for pais, color in asignacion.items():
        print(f"{pais}: {color}")
else:
    print("No se encontró solución.")
