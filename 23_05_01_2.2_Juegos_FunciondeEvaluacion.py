# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:25:18 2023

@author: carlo
En resumen, la función de evaluación es una herramienta clave en la inteligencia 
artificial aplicada a juegos, que se utiliza para determinar la mejor jugada posible 
en función de una serie de factores. Esta técnica se utiliza en combinación con algoritmos 
de búsqueda como el minimax con poda alfa-beta, y tiene aplicaciones en juegos como el 
ajedrez, el Go y otros juegos de mesa.

función de evaluación
"""

def evaluar_estado(tablero, jugador):
    oponente = 'O' if jugador == 'X' else 'X'
    puntaje = 0
    # Evaluar filas
    for fila in range(6):
        for columna in range(4):
            subsecuencia = tablero[fila][columna:columna+4]
            puntaje += evaluar_subsecuencia(subsecuencia, jugador, oponente)
    # Evaluar columnas
    for columna in range(7):
        for fila in range(3):
            subsecuencia = [tablero[fila+i][columna] for i in range(4)]
            puntaje += evaluar_subsecuencia(subsecuencia, jugador, oponente)
    # Evaluar diagonales ascendentes
    for columna in range(4):
        for fila in range(3, 6):
            subsecuencia = [tablero[fila-i][columna+i] for i in range(4)]
            puntaje += evaluar_subsecuencia(subsecuencia, jugador, oponente)
    # Evaluar diagonales descendentes
    for columna in range(4):
        for fila in range(3):
            subsecuencia = [tablero[fila+i][columna+i] for i in range(4)]
            puntaje += evaluar_subsecuencia(subsecuencia, jugador, oponente)
    return puntaje

def evaluar_subsecuencia(subsecuencia, jugador, oponente):
    if subsecuencia.count(jugador) == 4:
        return 100
    elif subsecuencia.count(jugador) == 3 and subsecuencia.count(' ') == 1:
        return 5
    elif subsecuencia.count(jugador) == 2 and subsecuencia.count(' ') == 2:
        return 2
    elif subsecuencia.count(oponente) == 3 and subsecuencia.count(' ') == 1:
        return -4
    else:
        return 0
