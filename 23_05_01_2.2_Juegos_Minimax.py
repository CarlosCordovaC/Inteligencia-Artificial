# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:41:09 2023

@author: carlo

El algoritmo funciona construyendo un árbol de juego que representa todas las posibles 
jugadas y sus consecuencias. A medida que el árbol se construye, se asigna un valor a 
cada nodo terminal (es decir, una situación en la que el juego ha terminado) que representa 
el resultado del juego para el jugador en cuestión.

Una vez que el árbol se ha construido, se realiza una búsqueda hacia atrás para determinar 
la mejor jugada posible en cada nivel del árbol. En cada nivel, se alternan las evaluaciones 
entre el jugador máximo (quien está tratando de maximizar su resultado) y el jugador mínimo 
(quien está tratando de minimizar el resultado del jugador máximo). El jugador máximo elegirá 
la jugada que maximice su resultado, mientras que el jugador mínimo elegirá la jugada 
que minimice el resultado del jugador máximo.

Minimax
"""
# Definir el tablero inicial del juego
tablero = [" ", " ", " ",
           " ", " ", " ",
           " ", " ", " "]

# Definir la función para imprimir el tablero
def imprimir_tablero(tablero):
    print(tablero[0] + "|" + tablero[1] + "|" + tablero[2])
    print("-+-+-")
    print(tablero[3] + "|" + tablero[4] + "|" + tablero[5])
    print("-+-+-")
    print(tablero[6] + "|" + tablero[7] + "|" + tablero[8])

# Definir la función para determinar si hay un ganador
def hay_ganador(tablero, jugador):
    # Comprobar las filas
    for i in range(0, 9, 3):
        if tablero[i] == jugador and tablero[i+1] == jugador and tablero[i+2] == jugador:
            return True
    # Comprobar las columnas
    for i in range(3):
        if tablero[i] == jugador and tablero[i+3] == jugador and tablero[i+6] == jugador:
            return True
    # Comprobar las diagonales
    if tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador:
        return True
    if tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador:
        return True
    return False

# Definir la función para determinar si el juego ha terminado
def juego_terminado(tablero):
    if " " not in tablero or hay_ganador(tablero, "X") or hay_ganador(tablero, "O"):
        return True
    return False

# Definir la función para obtener la lista de movimientos válidos
def obtener_movimientos(tablero):
    return [i for i in range(9) if tablero[i] == " "]

# Definir la función Minimax
def minimax(tablero, jugador):
    if hay_ganador(tablero, "X"):
        return -1
    elif hay_ganador(tablero, "O"):
        return 1
    elif " " not in tablero:
        return 0
    elif jugador == "O":
        mejor_valor = float("-inf")
        for movimiento in obtener_movimientos(tablero):
            nuevo_tablero = list(tablero)
            nuevo_tablero[movimiento] = jugador
            valor = minimax(nuevo_tablero, "X")
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for movimiento in obtener_movimientos(tablero):
            nuevo_tablero = list(tablero)
            nuevo_tablero[movimiento] = jugador
            valor = minimax(nuevo_tablero, "O")
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

# Definir la función para que la computadora realice un movimiento
def turno_computadora(tablero):
    mejor_movimiento = None
    mejor_valor = float("-inf")
    for movimiento in obtener_movimientos(tablero):
        nuevo_tablero = list(tablero)
        nuevo_tablero[movimiento] = "O"
        valor = minimax(nuevo_tablero, "X")
       
def turno_computadora(tablero):
    mejor_movimiento = None
    mejor_valor = float("-inf")
    for movimiento in obtener_movimientos(tablero):
        nuevo_tablero = list(tablero)
        nuevo_tablero[movimiento] = "O"
        valor = minimax(nuevo_tablero, "X")
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
            tablero[mejor_movimiento] = "O"
            
turno_jugador = True
while not juego_terminado(tablero):
    imprimir_tablero(tablero)
    if turno_jugador:
        movimiento_jugador = int(input("Ingresa el número de la casilla en la que deseas colocar tu marca (0-8): "))
        if tablero[movimiento_jugador] != " ":
            print("Esa casilla ya está ocupada, elige otra.")
            continue
        tablero[movimiento_jugador] = "X"
    else:
        turno_computadora(tablero)
        turno_jugador = not turno_jugador

imprimir_tablero(tablero)
if hay_ganador(tablero, "X"):
    print("¡Ganaste!")
elif hay_ganador(tablero, "O"):
    print("¡Perdiste!")
else:
    print("Empate")
