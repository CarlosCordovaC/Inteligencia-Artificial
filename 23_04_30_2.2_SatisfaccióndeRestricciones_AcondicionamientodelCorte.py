# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:18:13 2023

@author: carlo

Para resolver este problema, puedes utilizar el enfoque de satisfacción de restricciones 
con acondicionamiento del corte. Primero, definirías las restricciones: no más de 10 personas 
pueden estar en la casa al mismo tiempo, solo hay 3 sillas y algunos amigos no pueden estar 
en la casa al mismo tiempo.

Luego, utilizarías el acondicionamiento del corte para encontrar una solución que satisfaga 
todas las restricciones. Por ejemplo, podrías invitar a 5 amigos a una fiesta, asegurándote 
de que ninguno de los que no se llevan bien esté allí al mismo tiempo. Además, asegurándote 
de que solo haya 3 personas sentadas en cualquier momento y que no haya más de 10 personas en 
la casa en general.

"""

import random

# Definimos la función que comprueba si una lista es válida
def is_valid(lst):
    if len(lst) != 10:
        return False
    if any(x < 1 or x > 50 for x in lst):
        return False
    if sum(lst) != 250:
        return False
    return True

# Definimos una lista inicial aleatoria
lst = [random.randint(1, 50) for _ in range(10)]

# Definimos los dominios de los valores posibles para cada elemento
domains = {i: [x for x in range(1, 51)] for i in range(10)}

# Definimos el número máximo de iteraciones
max_iterations = 1000

# Aplicamos el algoritmo de Acondicionamiento del Corte
for i in range(max_iterations):
    # Seleccionamos un elemento al azar
    idx = random.randint(0, 9)
    
    # Si el valor actual no cumple las restricciones, seleccionamos uno nuevo
    if not is_valid(lst):
        lst[idx] = random.choice(domains[idx])
# Imprimimos el resultado final
print("Resultado final:", lst)


"""
En este ejemplo, la lista inicial se genera aleatoriamente y luego se aplican los pasos 
del algoritmo de Acondicionamiento del Corte. En cada iteración, se selecciona un elemento 
al azar y se comprueba si su valor actual cumple las restricciones. Si no las cumple, se 
selecciona un nuevo valor al azar dentro de su dominio. El algoritmo se detiene después de 
un número máximo de iteraciones o cuando se ha encontrado una lista que cumple las 
restricciones.
"""