# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:02:37 2023

@author: carlo

En resumen, el aprendizaje por refuerzo pasivo implica que un agente aprende a 
tomar decisiones óptimas basándose en datos históricos o ejemplos, en lugar de 
interactuar directamente con el entorno para recibir señales de refuerzo. 
El objetivo es que el agente aprenda un modelo del entorno y utilice ese modelo 
para tomar decisiones que maximicen las recompensas esperadas.
"""
import numpy as np

# Definir el entorno
# Supongamos que tenemos un entorno con 3 estados (0, 1, 2) y 2 acciones posibles (0, 1)
num_estados = 3
num_acciones = 2

# Definir las recompensas
recompensas = np.array([
    [-1, 0],
    [0, -1],
    [1, 1]
])

# Definir la matriz de transición
matriz_transicion = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])

# Definir hiperparámetros
num_episodios = 100
factor_aprendizaje = 0.5
factor_descuento = 0.9

# Inicializar la tabla Q con ceros
Q = np.zeros((num_estados, num_acciones))

# Aprendizaje por refuerzo pasivo
for _ in range(num_episodios):
    estado_actual = np.random.randint(0, num_estados)  # Estado inicial aleatorio

    while True:
        accion = np.argmax(Q[estado_actual])  # Seleccionar la acción con mayor valor Q
        
        nuevo_estado = np.random.choice(range(num_estados), p=matriz_transicion[estado_actual])  # Transición de estado
        
        recompensa = recompensas[estado_actual][accion]  # Obtener la recompensa

        # Actualizar el valor Q
        Q[estado_actual][accion] += factor_aprendizaje * (recompensa + factor_descuento * np.max(Q[nuevo_estado]) - Q[estado_actual][accion])

        estado_actual = nuevo_estado

        if estado_actual == num_estados - 1:  # Si alcanza el estado final, terminar el episodio
            break

# Imprimir la tabla Q resultante
print("Tabla Q:")
print(Q)

"""
En este ejemplo, el agente aprende a tomar decisiones óptimas en un entorno con 3 
estados y 2 acciones posibles. Cada acción tiene asociada una recompensa. 
El agente realiza transiciones de estado basadas en una matriz de transición y 
utiliza el algoritmo de Q-Learning para actualizar los valores Q en función de 
las recompensas recibidas. Después de un número de episodios de entrenamiento, 
el agente obtiene una tabla Q que representa los valores esperados de recompensa 
para cada par estado-acción. Esta tabla Q se puede utilizar para tomar decisiones 
óptimas en el entorno.
"""
