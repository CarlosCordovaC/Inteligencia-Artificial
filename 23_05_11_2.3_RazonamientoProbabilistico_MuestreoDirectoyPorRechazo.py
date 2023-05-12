# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:56 2023

@author: carlo

Muestreo Directo y Por Rechazo

En resumen, el muestreo directo y por rechazo son técnicas utilizadas en el 
razonamiento probabilístico para estimar probabilidades en modelos complejos. 
El muestreo directo genera muestras directamente del modelo, mientras que el muestreo 
por rechazo utiliza una distribución auxiliar y una regla de rechazo para estimar
probabilidades.

"""

import random

# Generar una lista de 1000 personas con atributo de cabello
personas = ['rubio'] * 600 + ['moreno'] * 400

# Muestreo directo
muestra_directa = random.sample(personas, 100)
proporcion_directa = muestra_directa.count('rubio') / len(muestra_directa)
print("Proporción de personas con cabello rubio (muestreo directo):", proporcion_directa)

# Muestreo por rechazo
submuestra = random.sample(personas, 50)
proporcion_submuestra = submuestra.count('rubio') / len(submuestra)
proporcion_rechazo = proporcion_submuestra * (len(personas) / len(submuestra))
print("Proporción de personas con cabello rubio (muestreo por rechazo):", proporcion_rechazo)
