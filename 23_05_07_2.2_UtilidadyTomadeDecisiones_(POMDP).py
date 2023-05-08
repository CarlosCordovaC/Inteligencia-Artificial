# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:24:17 2023

@author: carlo

En resumen, un POMDP es un modelo utilizado en inteligencia artificial para la 
toma de decisiones en entornos donde la información es parcialmente observada. 
Se utiliza un enfoque probabilístico para tomar decisiones secuenciales y maximizar 
la utilidad esperada a largo plazo. Sus aplicaciones son diversas y van desde asistentes 
virtuales hasta sistemas de control y diagnóstico en entornos inciertos.
"""

import random

# Definir los estados posibles
estados = ['Norte', 'Sur', 'Este', 'Oeste']

# Definir las acciones posibles
acciones = ['Girar derecha', 'Girar izquierda', 'Avanzar']

# Definir las observaciones posibles
observaciones = ['Nada', 'Ruido']

# Definir las recompensas por estado
recompensas = {
    'Norte': 10,
    'Sur': -10,
    'Este': 5,
    'Oeste': -5
}

# Definir la matriz de transición de estados
transiciones = {
    'Norte': {'Girar derecha': {'Norte': 0.8, 'Este': 0.2},
              'Girar izquierda': {'Norte': 0.8, 'Oeste': 0.2},
              'Avanzar': {'Norte': 1.0}},
    'Sur': {'Girar derecha': {'Sur': 0.8, 'Oeste': 0.2},
            'Girar izquierda': {'Sur': 0.8, 'Este': 0.2},
            'Avanzar': {'Sur': 1.0}},
    'Este': {'Girar derecha': {'Este': 0.8, 'Sur': 0.2},
             'Girar izquierda': {'Este': 0.8, 'Norte': 0.2},
             'Avanzar': {'Este': 1.0}},
    'Oeste': {'Girar derecha': {'Oeste': 0.8, 'Norte': 0.2},
              'Girar izquierda': {'Oeste': 0.8, 'Sur': 0.2},
              'Avanzar': {'Oeste': 1.0}}
}

# Definir la matriz de observaciones
observaciones_prob = {
    'Norte': {'Nada': 0.8, 'Ruido': 0.2},
    'Sur': {'Nada': 0.8, 'Ruido': 0.2},
    'Este': {'Nada': 0.8, 'Ruido': 0.2},
    'Oeste': {'Nada': 0.8, 'Ruido': 0.2}
}

# Función para realizar una acción y obtener una observación
def tomar_accion(estado, accion):
    nuevo_estado = random.choices(list(transiciones[estado][accion].keys()), list(transiciones[estado][accion].values()))[0]
    observacion = random.choices(observaciones, list(observaciones_prob[nuevo_estado].values()))[0]
    return nuevo_estado, observacion

# Función para calcular la utilidad esperada de una acción en un estado
def utilidad(estado, accion):
    utilidad_esperada = 0
    for nuevo_estado, prob_transicion in transiciones[estado][accion].items():
        utilidad_esperada += prob_transicion * recompensas[nuevo_estado]
    return utilidad_esperada

# Algoritmo de iteración de políticas para POMDP
def iteracion_politicas():
    politica = {estado: random.choice(acciones) for estado in estados}  # Política inicial aleatoria
    while True:
        nueva_politica = {}
        for estado in estados:        nueva_politica = {}
        for estado in estados:
            mejor_utilidad = float('-inf')
            mejor_accion = None
            for accion in acciones:
                utilidad_accion = utilidad(estado, accion)
                if utilidad_accion > mejor_utilidad:
                    mejor_utilidad = utilidad_accion
                    mejor_accion = accion
            nueva_politica[estado] = mejor_accion
        if nueva_politica == politica:
            break
        politica = nueva_politica
    return politica

# Ejecutar el algoritmo de iteración de políticas
politica_optima = iteracion_politicas()

# Imprimir la política óptima
print("Política óptima:")
for estado, accion in politica_optima.items():
    print(f"Estado: {estado} - Acción: {accion}")

