# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:51:55 2023

@author: carlo
"""

from constraint import *

# Creamos el problema
problem = Problem()

# Definimos las variables
variables = ["a", "b", "c"]
problem.addVariables(variables, range(1, 11))

# Definimos las restricciones
def suma_igual_10(a, b, c):
    if a + b + c == 10:
        return True

def multiplicacion_igual_24(a, b, c):
    if a * b * c == 24:
        return True

problem.addConstraint(suma_igual_10, variables)
problem.addConstraint(multiplicacion_igual_24, variables)

# Resolvemos el problema
solutions = problem.getSolutions()

print(solutions)
