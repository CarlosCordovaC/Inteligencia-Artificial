# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:53:29 2023

@author: carlo

Un ejemplo de la vida diaria en el que se podría aplicar el Salto Atrás Dirigido por 
Conflictos podría ser la planificación de un menú semanal para una familia que tiene 
restricciones dietéticas y culinarias. Cada día, la familia debe decidir qué cocinar para 
el desayuno, el almuerzo y la cena, teniendo en cuenta las preferencias personales de cada 
miembro de la familia, las restricciones dietéticas (como alergias o intolerancias) y los 
ingredientes disponibles. Además, la familia puede querer asegurarse de que están comiendo 
una dieta balanceada y variada. Utilizando el Salto Atrás Dirigido por Conflictos, se podrían
 hacer las decisiones en orden secuencial y ajustar el menú cada vez que se encuentre una 
 restricción conflictiva, como la imposibilidad de cocinar un plato debido a la falta de 
 ingredientes o alergias.
 
 Salto Atrás Dirigido
 
"""

from constraint import *

problem = Problem()

# Creamos una lista de variables con valores únicos
variables = ['a', 'b', 'c', 'd', 'e']

# Agregamos las variables al problema con dominio de 1 a 5
for variable in variables:
    problem.addVariable(variable, range(1, 6))

# Agregamos la restricción de que el valor de cada variable sea mayor que el valor de la variable anterior en la lista
for i in range(len(variables) - 1):
    problem.addConstraint(lambda a, b: a < b, (variables[i], variables[i + 1]))

# Agregamos la restricción de que el valor de cada variable sea menor que el valor de la variable siguiente en la lista
for i in range(1, len(variables)):
    problem.addConstraint(lambda a, b: a < b, (variables[i - 1], variables[i]))

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones
for solution in solutions:
    print(solution)


"""
En este ejemplo, estamos creando un problema que consiste en asignar valores únicos 
a cada variable en la lista ['a', 'b', 'c', 'd', 'e']. Para ello, agregamos las variables 
al problema y les asignamos un dominio de 1 a 5. Luego, agregamos dos restricciones: 
una que asegura que el valor de cada variable sea mayor que el valor de la variable 
anterior en la lista, y otra que asegura que el valor de cada variable sea menor que 
el valor de la variable siguiente en la lista. Finalmente, resolvemos el problema y 
mostramos las soluciones encontradas.
"""