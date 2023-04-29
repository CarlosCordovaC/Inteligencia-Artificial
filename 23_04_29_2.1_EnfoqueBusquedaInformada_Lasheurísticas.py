# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:55:46 2023

@author: carlo

Por ejemplo, en el juego de ajedrez, una heurística puede ser la evaluación de la posición 
de las piezas en el tablero, basada en factores como la movilidad, la protección del rey, 
la cantidad y valor de las piezas, entre otros. Esta evaluación puede utilizarse para estimar
la probabilidad de que un movimiento dado lleve a una posición mejor o peor en el siguiente 
turno.

Las heurísticas
"""

from queue import PriorityQueue

# Estado objetivo del 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Función para calcular la heurística
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                row = (value - 1) // 3
                col = (value - 1) % 3
                distance += abs(row - i) + abs(col - j)
    return distance

# Función para obtener el movimiento que se hizo para llegar al estado actual
def get_move(prev_state, curr_state):
    for i in range(3):
        for j in range(3):
            if prev_state[i][j] != curr_state[i][j]:
                if j > 0 and curr_state[i][j-1] == prev_state[i][j]:
                    return 'left'
                elif j < 2 and curr_state[i][j+1] == prev_state[i][j]:
                    return 'right'
                elif i > 0 and curr_state[i-1][j] == prev_state[i][j]:
                    return 'up'
                elif i < 2 and curr_state[i+1][j] == prev_state[i][j]:
                    return 'down'

# Función para obtener los estados adyacentes
def get_adjacent_states(state):
    row, col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j
    adjacent_states = []
    if row > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
        adjacent_states.append(new_state)
    if row < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
        adjacent_states.append(new_state)
    if col > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
        adjacent_states.append(new_state)
    if col < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
        adjacent_states.append(new_state)
    return adjacent_states

# Función para resolver el 8-puzzle utilizando el algoritmo A*
def solve(start_state):
    frontier = PriorityQueue()
    frontier.put((0, start_state))
    came_from = {}
    cost_so_far = {}
    came_from[str(start_state)] = None
    cost_so_far[str(start_state)] = 0
    while not frontier.empty():
        _, current_state = frontier.get()
        if current_state == goal_state:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = came_from[str(current_state)]
            path.reverse()
            return path
        for next_state in get_adjacent_states(current_state):
            new_cost = cost_so_far[str(current_state)] + 1
            if str(next_state) not in cost_so_far or new_cost < cost_so_far[str(next_state)]:
                cost_so_far[str(next_state)] = new_cost
                priority = new_cost + manhattan_distance(next_state)
                frontier.put((priority, next_state))
                came_from[str(next_state)] = current_state
    return None

"""
Este código resuelve el problema del 8-puzzle utilizando el algoritmo A*. El 8-puzzle es 
un juego en el que se tienen 8 fichas numeradas y un espacio vacío en una cuadrícula de 
3x3. El objetivo del juego es mover las fichas para alcanzar una configuración objetivo 
en la que los números estén en orden ascendente y el espacio vacío esté en la esquina 
inferior derecha.
"""