# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:48:06 2023

@author: carlo

 imagina que tienes una caja de lápices de colores y quieres colorear una imagen. 
 Sin embargo, cada sección de la imagen tiene restricciones sobre qué colores se 
 pueden usar. Por ejemplo, la sección superior izquierda solo puede ser amarilla o 
 roja, y la sección inferior derecha solo puede ser verde o azul.
"""
def satisface_restricciones(variables, restricciones, asignacion):
    for restriccion in restricciones:
        var1, var2, funcion_restriccion = restriccion
        if var1 in asignacion and var2 in asignacion:
            if not funcion_restriccion(asignacion[var1], asignacion[var2]):
                return False
    return True


def asigna_valores(variables, restricciones, asignacion):
    if len(asignacion) == len(variables):
        return asignacion
    var_no_asignada = [v for v in variables if v not in asignacion][0]
    for valor in range(1, 6):
        asignacion[var_no_asignada] = valor
        if satisface_restricciones(variables, restricciones, asignacion):
            resultado = asigna_valores(variables, restricciones, asignacion)
            if resultado is not None:
                return resultado
        del asignacion[var_no_asignada]
    return None


variables = ['x', 'y', 'z']
restricciones = [
    ('x', 'y', lambda x, y: x + y == 5),
    ('y', 'z', lambda y, z: y - z == 1)
]

asignacion = {}
solucion = asigna_valores(variables, restricciones, asignacion)
print(solucion)
