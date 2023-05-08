# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:49:56 2023

@author: carlo

Imaginemos que eres un estudiante universitario y compartes un apartamento con un 
compañero de cuarto. Tú y tu compañero deben decidir quién se encargará de lavar 
los platos después de la cena. Hay dos opciones disponibles: uno de ustedes puede 
lavar los platos o pueden acordar turnarse para hacerlo.

Este escenario se puede modelar como un juego de coordinación en la Teoría de Juegos. 
Cada opción tiene su propio resultado preferido:

Ambos lavan los platos: Esto es beneficioso para ambos, ya que comparten las tareas y 
pueden disfrutar de un apartamento limpio.

Turnarse para lavar los platos: Esto también es aceptable, ya que ambos tienen la 
responsabilidad compartida y no recae completamente en uno solo.

Sin embargo, hay un tercer resultado que ambos prefieren evitar:

Ninguno lava los platos: Esto llevará a un apartamento desordenado y platos sucios acumulados.
En este caso, el Equilibrio de Nash sería que ambos elijan la opción de "Ambos lavan 
los platos". Ninguno de ustedes tiene incentivos para cambiar su estrategia, ya que no 
quieren enfrentarse al resultado no deseado de platos sucios acumulados.

Aquí, la Teoría de Juegos proporciona una forma de analizar y entender las dinámicas de 
toma de decisiones entre tú y tu compañero de cuarto. Puedes aplicar los conceptos de 
equilibrio y estrategia para encontrar soluciones que satisfagan a ambos y eviten conflictos 
en la asignación de tareas domésticas.
"""

import nashpy as nash

# Definir las matrices de pagos para cada jugador
jugador1 = [[2, -1], [0, 1]]
jugador2 = [[1, -2], [-1, 0]]

# Crear el juego con las matrices de pagos
juego = nash.Game(jugador1, jugador2)

# Calcular el equilibrio de Nash del juego
equilibrio_nash = juego.support_enumeration()

# Imprimir los equilibrios de Nash encontrados
print("Equilibrios de Nash encontrados:")
for eq in equilibrio_nash:
    print(eq)

