# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:47:57 2023

@author: carlo

Un ejemplo de cómo se puede aplicar el aprendizaje basado en el conocimiento en la 
vida diaria es en la planificación de un menú semanal de comidas. Un experto en nutrición 
puede proporcionar reglas lógicas que establezcan relaciones entre diferentes nutrientes y 
alimentos. Por ejemplo, puede establecer una regla que diga que es necesario consumir una 
cierta cantidad de proteínas y vitaminas en cada comida. Con estas reglas, se puede 
desarrollar un sistema que tome en cuenta las preferencias de los usuarios y sugiera 
comidas que cumplan con estas reglas, ayudando a mejorar la salud y nutrición de las 
personas.

Aprendizaje Basado en el Conocimiento
"""

def longitud_petalos_corta(flor):
    return flor['longitud_petalos'] < 2.5

def longitud_petalos_media(flor):
    return 2.5 <= flor['longitud_petalos'] < 5.0

def longitud_petalos_larga(flor):
    return flor['longitud_petalos'] >= 5.0

def anchura_petalos_angosta(flor):
    return flor['anchura_petalos'] < 1.0

def anchura_petalos_media(flor):
    return 1.0 <= flor['anchura_petalos'] < 1.8

def anchura_petalos_ancha(flor):
    return flor['anchura_petalos'] >= 1.8

def clase_setosa(flor):
    return flor['clase'] == 'setosa'

def clase_versicolor(flor):
    return flor['clase'] == 'versicolor'

def clase_virginica(flor):
    return flor['clase'] == 'virginica'

reglas = [
    ((clase_setosa, [longitud_petalos_corta, anchura_petalos_angosta])),
    ((clase_versicolor, [longitud_petalos_media, anchura_petalos_media])),
    ((clase_virginica, [longitud_petalos_larga, anchura_petalos_ancha]))
]

nueva_flor = {'longitud_petalos': 4.9, 'anchura_petalos': 1.3}
clase = None

for regla in reglas:
    if all(predicado(nueva_flor) for predicado in regla[1]):
        clase = regla[0].__name__
        break

print(f'La nueva flor es de la clase {clase}')


"""
Este código utiliza las funciones definidas para determinar la clase de una flor 
desconocida basándose en reglas. Las reglas son una lista de tuplas, donde cada 
tupla representa una regla que dice qué clase es la flor si se cumplen ciertas 
condiciones. Por ejemplo, la regla (clase_setosa, [longitud_petalos_corta, 
anchura_petalos_angosta]) dice que si una flor tiene una longitud de pétalos 
inferior a 2.5 y una anchura de pétalos inferior a 1.0, entonces es de la clase 'setosa'.

Luego, se define una nueva flor con una longitud de pétalos de 4.9 y una anchura de
pétalos de 1.3. El código evalúa cada regla en la lista de reglas, y si se cumplen 
todas las condiciones de la regla, entonces la flor se clasifica como la clase 
correspondiente. En este caso, la flor se clasifica como 'versicolor'. Finalmente, 
se imprime un mensaje indicando la clase a la que pertenece la nueva flor.
"""