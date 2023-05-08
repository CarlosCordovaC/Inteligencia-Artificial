# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:14:04 2023

@author: carlo

En resumen, el MDP es un marco teórico y matemático ampliamente utilizado en 
inteligencia artificial para modelar problemas de toma de decisiones secuenciales en 
entornos estocásticos. Permite encontrar políticas óptimas que maximicen la utilidad 
o recompensa acumulada a largo plazo. Sus aplicaciones son variadas y pueden ser 
utilizadas en diversas áreas de la vida diaria.

"""

import random

# Definir el espacio de estados y acciones
estados = ['Bajo', 'Medio', 'Alto']
acciones = ['Adivinar', 'Incrementar', 'Decrementar']

# Definir las recompensas para cada estado
recompensas = {
    'Bajo': {'Adivinar': 10, 'Incrementar': 1, 'Decrementar': -1},
    'Medio': {'Adivinar': 20, 'Incrementar': 2, 'Decrementar': -2},
    'Alto': {'Adivinar': 30, 'Incrementar': -10, 'Decrementar': -10}
}

# Definir la función de transición
def transicion(estado, accion):
    if accion == 'Adivinar':
        return random.choice(estados)  # El nuevo estado es aleatorio
    elif accion == 'Incrementar':
        index = estados.index(estado)
        if index < len(estados) - 1:
            return estados[index + 1]  # Incrementar el estado
        else:
            return estado  # Permanecer en el estado actual
    elif accion == 'Decrementar':
        index = estados.index(estado)
        if index > 0:
            return estados[index - 1]  # Decrementar el estado
        else:
            return estado  # Permanecer en el estado actual

# Función de utilidad para obtener la recompensa esperada
def utilidad(estado, accion):
    return recompensas[estado][accion]

# Algoritmo de iteración de políticas
def iteracion_politicas():
    politica = {estado: random.choice(acciones) for estado in estados}  # Política inicial aleatoria
    while True:
        nueva_politica = {}
        for estado in estados:
            mejor_accion = None
            mejor_utilidad = float('-inf')
            for accion in acciones:
                nueva_utilidad = utilidad(estado, accion)
                nuevo_estado = transicion(estado, accion)
                utilidad_esperada = utilidad(nuevo_estado, politica[nuevo_estado])  # Utilidad esperada
                nueva_utilidad += utilidad_esperada
                if nueva_utilidad > mejor_utilidad:
                    mejor_utilidad = nueva_utilidad
                    mejor_accion = accion
            nueva_politica[estado] = mejor_accion
        if nueva_politica == politica:  # Si la política no cambia, hemos encontrado la óptima
            break
        politica = nueva_politica
    return politica

# Ejecutar el algoritmo de iteración de políticas
politica_optima = iteracion_politicas()

# Imprimir la política óptima resultante
print("Política óptima:")
for estado in estados:
    print(f"Estado: {estado} - Acción: {politica_optima[estado]}")
    

"""
El algoritmo de Iteración de Políticas se ejecuta iterativamente para mejorar la 
política en cada iteración. Se selecciona una política inicial aleatoria y se evalúan 
todas las acciones posibles para cada estado. Se calcula la utilidad esperada considerando 
la recompensa actual y la utilidad esperada del siguiente estado según la política actual. 
Se selecciona la mejor acción en cada estado y se actualiza la política. El proceso se 
repite hasta que la política no cambie, lo que indica que se ha encontrado la política 
óptima.

Al final, se imprime la política óptima resultante, que muestra la acción recomendada 
para cada estado.
"""

