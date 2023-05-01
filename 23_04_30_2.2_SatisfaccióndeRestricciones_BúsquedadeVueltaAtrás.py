# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:02:02 2023

@author: carlo
Un ejemplo de cómo la búsqueda de vuelta atrás se puede aplicar a la vida diaria es la 
planificación de una fiesta de cumpleaños. Supongamos que se tiene una lista de tareas que 
se deben completar antes de la fiesta, como comprar la comida, decorar el lugar, y enviar 
las invitaciones. Cada tarea tiene una restricción de tiempo, es decir, una fecha límite para 
su realización. Además, hay una lista de posibles fechas para la fiesta.

Para encontrar la fecha ideal para la fiesta, se puede utilizar la búsqueda de vuelta atrás. 
Se puede comenzar asignando una fecha a la fiesta y verificar si se pueden completar todas 
las tareas antes de la fecha límite correspondiente. Si no es posible, el algoritmo retrocede 
y prueba con otra fecha hasta encontrar una que cumpla con todas las restricciones.

Búsqueda de Vuelta Atrás
"""

# Definir la lista de países y sus vecinos
paises = {'A': ['B', 'C', 'D'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['A', 'C']}
colores_disponibles = ['rojo', 'azul', 'verde']

# Función que verifica si el país puede ser coloreado con un color en particular
def es_color_valido(pais, color, solucion):
    for vecino in paises[pais]:
        if vecino in solucion and solucion[vecino] == color:
            return False
    return True

# Función que implementa la búsqueda de vuelta atrás
def resolver_mapa(paises, colores_disponibles, solucion):
    # Verificar si se ha encontrado una solución completa
    if len(solucion) == len(paises):
        return solucion
    
    # Seleccionar un país no coloreado
    pais = None
    for p in paises:
        if p not in solucion:
            pais = p
            break
    
    # Intentar colorear el país con cada color disponible
    for color in colores_disponibles:
        if es_color_valido(pais, color, solucion):
            solucion[pais] = color
            resultado = resolver_mapa(paises, colores_disponibles, solucion)
            if resultado is not None:
                return resultado
            solucion.pop(pais)
    
    # No se encontró ninguna solución
    return None

# Ejecutar la búsqueda de vuelta atrás
solucion = resolver_mapa(paises, colores_disponibles, {})
print(solucion)

"""
Este código resolverá el problema de colorear un mapa usando la técnica de búsqueda 
de vuelta atrás. La función resolver_mapa es la que implementa la lógica de la búsqueda 
de vuelta atrás, y la función es_color_valido es una función auxiliar que verifica si un 
país puede ser coloreado con un color en particular sin violar las restricciones de que 
dos países vecinos no pueden tener el mismo color. La solución final es un diccionario 
que asigna a cada país un color.
"""
