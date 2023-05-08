# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:38:44 2023

@author: carlo
"""
import random

# Definir los posibles estados de actividad y calidad del sueño
estados_actividad = ['Alta', 'Media', 'Baja']
estados_sueno = ['Buena', 'Regular', 'Mala']

# Definir la matriz de transición de estados de actividad
transiciones_actividad = {
    'Alta': {'Alta': 0.7, 'Media': 0.2, 'Baja': 0.1},
    'Media': {'Alta': 0.3, 'Media': 0.4, 'Baja': 0.3},
    'Baja': {'Alta': 0.1, 'Media': 0.3, 'Baja': 0.6}
}

# Definir la matriz de transición de estados de calidad del sueño
transiciones_sueno = {
    'Buena': {'Buena': 0.7, 'Regular': 0.2, 'Mala': 0.1},
    'Regular': {'Buena': 0.3, 'Regular': 0.4, 'Mala': 0.3},
    'Mala': {'Buena': 0.1, 'Regular': 0.3, 'Mala': 0.6}
}

# Función para realizar una transición de estado dado un estado actual y una matriz de transición
def transicion_estado(estado_actual, matriz_transicion):
    if estado_actual in matriz_transicion:
        return random.choices(list(matriz_transicion[estado_actual].keys()), list(matriz_transicion[estado_actual].values()))[0]
    else:
        raise ValueError(f"El estado {estado_actual} no se encuentra en la matriz de transición.")

# Función para simular las elecciones diarias de ejercicio y hora de dormir
def simular_dia():
    nivel_ejercicio = random.choice(estados_actividad)
    hora_dormir = random.choice(estados_sueno)
    return nivel_ejercicio, hora_dormir

# Función para predecir el estado de actividad y calidad del sueño en el futuro dado un estado inicial
def predecir_estado_futuro(estado_inicial, pasos):
    estado_actividad = estado_inicial
    estado_sueno = estado_inicial
    for _ in range(pasos):
        estado_actividad = transicion_estado(estado_actividad, transiciones_actividad)
        estado_sueno = transicion_estado(estado_sueno, transiciones_sueno)
    return estado_actividad, estado_sueno

# Ejemplo de uso
estado_inicial_actividad = random.choice(estados_actividad)
estado_inicial_sueno = random.choice(estados_sueno)
print("Estado inicial de actividad:", estado_inicial_actividad)
print("Estado inicial de sueño:", estado_inicial_sueno)


ejercicio_actual, hora_dormir_actual = simular_dia()
print("Ejercicio actual:", ejercicio_actual)
print("Hora de dormir actual:", hora_dormir_actual)







