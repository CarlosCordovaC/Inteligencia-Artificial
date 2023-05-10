# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:03:06 2023

@author: carlo

En resumen, la Regla de Bayes nos permite actualizar nuestras creencias sobre un evento 
o hipótesis en función de la evidencia disponible. Es una herramienta fundamental en la
 inteligencia artificial para realizar inferencias probabilísticas y tomar decisiones 
 basadas en datos observados.
"""

# Probabilidades a priori
p_a = 0.5  # Probabilidad de seleccionar la Caja A
p_b = 0.5  # Probabilidad de seleccionar la Caja B

# Probabilidades condicionales
p_r_a = 5 / 8  # Probabilidad de obtener una bola roja dado que se selecciona la Caja A
p_r_b = 4 / 10  # Probabilidad de obtener una bola roja dado que se selecciona la Caja B

# Aplicando la Regla de Bayes
p_a_r = (p_r_a * p_a) / ((p_r_a * p_a) + (p_r_b * p_b))

print("La probabilidad de que la bola provenga de la Caja A dado que es roja es:", p_a_r)


"""
En este ejemplo, utilizamos la Regla de Bayes para calcular la probabilidad a 
posteriori de que la bola provenga de la Caja A, dado que hemos obtenido una bola roja. 
La probabilidad a priori de seleccionar la Caja A y la Caja B es igual (0.5 en este caso). 
Las probabilidades condicionales se calculan dividiendo el número de bolas rojas en cada 
caja por el número total de bolas en esa caja.

El resultado impreso será la probabilidad a posteriori de que la bola provenga de la Caja 
A dado que es roja. En este ejemplo, la probabilidad es 0.625, lo que significa que hay 
una alta probabilidad de que la bola provenga de la Caja A después de haber obtenido una 
bola roja.
"""