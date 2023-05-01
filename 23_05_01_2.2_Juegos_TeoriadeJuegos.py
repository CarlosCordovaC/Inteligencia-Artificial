# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:30:16 2023

@author: carlo

Un ejemplo de cómo se puede aplicar la Teoría de Juegos en la vida diaria es en la 
toma de decisiones en una competencia deportiva como el tenis. Supongamos que dos 
jugadores tienen habilidades similares y están jugando un partido importante. Cada 
jugador debe tomar decisiones estratégicas sobre dónde colocar la pelota y qué tipo de 
golpe usar para intentar ganar puntos. En este caso, se puede utilizar la Teoría de 
Juegos para modelar el comportamiento de cada jugador y encontrar la estrategia óptima 
que maximice la probabilidad de ganar el partido.

"""

import random

# Definir las opciones del juego
opciones = ["piedra", "papel", "tijeras"]

# Definir la función que determina el ganador
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return 0
    elif (opcion1 == "piedra" and opcion2 == "tijeras") or (opcion1 == "tijeras" and opcion2 == "papel") or (opcion1 == "papel" and opcion2 == "piedra"):
        return 1
    else:
        return 2

# Definir el juego
juego_terminado = False
while not juego_terminado:
    # Pedir a los jugadores que elijan una opción
    opcion_jugador1 = input("Jugador 1, elige una opción (piedra, papel o tijeras): ")
    opcion_jugador2 = random.choice(opciones)
    print("Jugador 2 ha elegido", opcion_jugador2)

    # Determinar el ganador
    ganador = determinar_ganador(opcion_jugador1, opcion_jugador2)
    if ganador == 0:
        print("Empate, vuelvan a jugar")
    elif ganador == 1:
        print("¡Jugador 1 ha ganado!")
        juego_terminado = True
    else:
        print("¡Jugador 2 ha ganado!")
        juego_terminado = True
