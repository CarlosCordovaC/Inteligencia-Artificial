# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:39:13 2023

@author: carlo

Un ejemplo de cómo se podría utilizar la búsqueda Minimax Esperado en la vida diaria 
es en la toma de decisiones empresariales. Por ejemplo, si una empresa está considerando 
lanzar un nuevo producto, puede utilizar la búsqueda Minimax Esperado para evaluar las 
posibles respuestas de la competencia y decidir si el lanzamiento del producto es una buena 
opción. La empresa podría asumir que la competencia tomará la mejor decisión en su propio 
interés, pero que también hay una cierta probabilidad de que la competencia tome una decisión 
subóptima. En función de esta información, la empresa podría tomar una decisión informada 
sobre si lanzar o no el producto.


"""
import random
import math

def minimax_esperado(estado, profundidad):
    if profundidad == 0:
        return evaluar(estado), None

    mejor_valor = -math.inf
    mejor_movimiento = None
    for movimiento in ["cara", "cruz"]:
        valor_probabilistico = 0
        for i in range(10):
            resultado = random.choice(["cara", "cruz"])
            if resultado == movimiento:
                valor_probabilistico += 2
            else:
                valor_probabilistico += 1
        valor_probabilistico /= 10
        valor, _ = minimax_esperado(resultado, profundidad - 1)
        valor_probabilistico += valor
        if valor_probabilistico > mejor_valor:
            mejor_valor = valor_probabilistico
            mejor_movimiento = movimiento

    return mejor_valor, mejor_movimiento

def evaluar(estado):
    valor_probabilistico_cara = 0
    valor_probabilistico_cruz = 0
    for i in range(10):
        resultado = random.choice(["cara", "cruz"])
        if resultado == "cara":
            valor_probabilistico_cara += 2
        else:
            valor_probabilistico_cruz += 1
    valor_probabilistico_cara /= 10
    valor_probabilistico_cruz /= 10
    return max(valor_probabilistico_cara, valor_probabilistico_cruz)

valor, movimiento = minimax_esperado(None, 2)
print("El movimiento recomendado es:", movimiento)
print("Valor esperado del movimiento recomendado:", valor)

