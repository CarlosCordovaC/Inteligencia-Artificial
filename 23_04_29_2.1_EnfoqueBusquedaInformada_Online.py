# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:22:31 2023

@author: carlo

Un ejemplo más concreto de aplicación de búsqueda online podría ser en un sistema de 
recomendación de películas o series de televisión. En lugar de presentar todas las opciones 
disponibles de una sola vez, el sistema puede presentar recomendaciones basadas en las 
preferencias del usuario y en tiempo real ir ajustando las recomendaciones a medida que 
el usuario va dando feedback.

Busqueda Online
"""

def online_search(target, nums):
    found = False
    for i in range(len(nums)):
        if nums[i] == target:
            found = True
            break
    return found

# Ejemplo de uso:
nums = [5, 2, 8, 3, 9, 1]
target = 8
if online_search(target, nums):
    print("El número objetivo se encontró en la lista.")
else:
    print("El número objetivo no se encontró en la lista.")


"""
En este ejemplo, la función online_search recibe dos argumentos: target, que es el 
número que se está buscando, y nums, que es la lista de números en la que se buscará. 
La función recorre la lista de números uno por uno y compara cada número con el número 
objetivo. Si el número objetivo se encuentra en la lista, la función devuelve True. De 
lo contrario, devuelve False.
"""