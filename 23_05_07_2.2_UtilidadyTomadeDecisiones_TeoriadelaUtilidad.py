# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:28:54 2023

@author: carlo

Un ejemplo de la vida diaria podría ser la elección de un restaurante para cenar. 
Supongamos que tenemos tres opciones: un restaurante de comida rápida, un restaurante 
de comida italiana y un restaurante de comida china. Si nuestro agente inteligente está 
programado para maximizar la satisfacción del cliente, podría utilizar una función de 
utilidad para asignar un valor numérico a cada opción en función de las preferencias del 
cliente. Podría tener en cuenta factores como el precio, la calidad de la comida, la 
distancia y la variedad del menú. Luego, el agente podría utilizar la teoría de la utilidad 
para comparar las opciones y seleccionar el restaurante que maximice la satisfacción del 
cliente.

Teoría de la Utilidad: Función de Utilidad
"""

def calcular_utilidad(opcion):
    # Aquí se calcula la utilidad de una opción específica
    # basada en criterios relevantes para tu problema

    # Supongamos que la utilidad se calcula en una escala de 0 a 100
    if opcion == "opcion_1":
        return 80
    elif opcion == "opcion_2":
        return 90
    elif opcion == "opcion_3":
        return 70

def tomar_decision(opciones):
    mejor_opcion = None
    mejor_utilidad = float('-inf')

    for opcion in opciones:
        utilidad = calcular_utilidad(opcion)
        if utilidad > mejor_utilidad:
            mejor_opcion = opcion
            mejor_utilidad = utilidad

    return mejor_opcion

# Ejemplo de uso
opciones_disponibles = ["opcion_1", "opcion_2", "opcion_3"]
mejor_opcion = tomar_decision(opciones_disponibles)

print("La mejor opción es:", mejor_opcion)
