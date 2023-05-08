# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:02:22 2023

@author: carlo

Un ejemplo de aplicación de la Iteración de Valores en la vida diaria podría ser 
la negociación de precios entre vendedores y compradores en un mercado. Supongamos 
que eres un vendedor en un mercado competitivo y debes determinar el precio óptimo 
para tu producto. Existen múltiples compradores con diferentes preferencias y 
restricciones presupuestarias.


Para utilizar la Iteración de Valores, puedes asignar un valor a cada 
combinación posible de precios y acciones de los compradores. Luego, iterativamente, 
actualizas los valores de los precios considerando las preferencias y decisiones de 
los compradores. Continúas este proceso hasta que los valores converjan a un equilibrio 
en el que ningún comprador puede mejorar su posición cambiando su estrategia de compra 
o presupuesto.

Este enfoque te permitiría determinar el precio óptimo para maximizar tus ganancias y 
alcanzar un equilibrio en el mercado. Cada comprador también tomaría decisiones óptimas 
en función de los valores de los precios y las acciones de los demás compradores.
"""

import numpy as np

# Matriz de pagos
payoff_matrix = np.array([[4, 1], [6, 2]])

# Inicialización de valores de los estados
player1_values = np.zeros((2, 2))
player2_values = np.zeros((2, 2))

# Iteración de Valores
iterations = 100
for _ in range(iterations):
    for i in range(2):
        for j in range(2):
            # Calcula el valor del estado para el jugador 1
            player1_values[i, j] = payoff_matrix[i, j] + max(
                0.8 * player1_values[0, j] + 0.2 * player1_values[1, j],
                0.8 * player1_values[i, 0] + 0.2 * player1_values[i, 1],
            )

            # Calcula el valor del estado para el jugador 2
            player2_values[i, j] = payoff_matrix[i, j] + max(
                0.8 * player2_values[0, j] + 0.2 * player2_values[1, j],
                0.8 * player2_values[i, 0] + 0.2 * player2_values[i, 1],
            )

# Imprime los valores finales de los estados
print("Valores finales para el jugador 1:")
print(player1_values)
print("Valores finales para el jugador 2:")
print(player2_values)
