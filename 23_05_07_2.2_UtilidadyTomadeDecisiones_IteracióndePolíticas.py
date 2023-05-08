# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:08:05 2023

@author: carlo

Un ejemplo de la vida diaria podría ser la toma de decisiones sobre inversiones 
financieras. Supongamos que eres un inversor y debes decidir en qué acciones invertir. 
Mediante la Iteración de Políticas, puedes desarrollar una estrategia óptima que tenga 
en cuenta factores como el rendimiento pasado de las acciones, las condiciones del mercado 
y las expectativas de ganancias futuras. El algoritmo evaluará y mejorará continuamente 
tu política de inversión, permitiéndote tomar decisiones más informadas y maximizar tu 
rendimiento financiero a lo largo del tiempo.
"""

import numpy as np

# Definir el laberinto (0: camino libre, 1: obstáculo, 2: salida)
laberinto = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 2]
])

# Definir la política inicial (0: izquierda, 1: arriba, 2: derecha, 3: abajo)
politica = np.zeros_like(laberinto)

# Definir las recompensas por cada estado
recompensas = np.zeros_like(laberinto)
recompensas[laberinto == 2] = 1  # Recompensa positiva en la salida

# Iteración de Políticas
num_iteraciones = 100
for _ in range(num_iteraciones):
    nuevos_valores = np.zeros_like(recompensas)
    
    # Para cada estado en el laberinto
    for i in range(laberinto.shape[0]):
        for j in range(laberinto.shape[1]):
            if laberinto[i, j] == 2:  # Si es la salida, pasar al siguiente estado
                nuevos_valores[i, j] = 0
                continue
            
            # Calcular el valor para cada acción en el estado actual
            valores_acciones = []
            for accion in range(4):
                if accion == 0:  # Izquierda
                    if j > 0 and laberinto[i, j-1] != 1:
                        valores_acciones.append(recompensas[i, j-1] + nuevos_valores[i, j-1])
                    else:
                        valores_acciones.append(-np.inf)
                elif accion == 1:  # Arriba
                    if i > 0 and laberinto[i-1, j] != 1:
                        valores_acciones.append(recompensas[i-1, j] + nuevos_valores[i-1, j])
                    else:
                        valores_acciones.append(-np.inf)
                elif accion == 2:  # Derecha
                    if j < laberinto.shape[1] - 1 and laberinto[i, j+1] != 1:
                        valores_acciones.append(recompensas[i, j+1] + nuevos_valores[i, j+1])
                    else:
                        valores_acciones.append(-np.inf)
                elif accion == 3:  # Abajo
                    if i < laberinto.shape[0] - 1 and laberinto[i+1, j] != 1:
                        valores_acciones.append(recompensas[i+1, j] + nuevos_valores[i+1, j])
                    else:
                        valores_acciones.append(-np.inf)
            
            # Asignar el valor máximo como el nuevo valor del estado
            nuevos_valores[i, j] = np.max(valores_acciones)
    
    # Actualizar la política basada en los nuevos valores
    politica = np.argmax(nuevos_valores, axis=2)
    
# Imprimir la política resultante
print(politica)
