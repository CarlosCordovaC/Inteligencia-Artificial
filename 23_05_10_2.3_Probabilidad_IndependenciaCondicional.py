# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:57:10 2023

@author: carlo

La independencia condicional establece que la ocurrencia de dos eventos A y B 
puede ser independiente cuando se condicionan a un tercer evento C. Esto implica que 
la probabilidad de que ocurra A no se ve afectada por la ocurrencia de B una vez que 
se conoce C. Es un concepto importante en inteligencia artificial y probabilidades, 
ya que permite modelar relaciones entre eventos y hacer suposiciones basadas en la 
independencia de ciertas variables.
"""

import pandas as pd
from scipy.stats import chi2_contingency

# Crear un DataFrame simulado
data = pd.DataFrame({
    'Deporte': ['F', 'B', 'F', 'B', 'F', 'B', 'F', 'B'],
    'Sombrero': ['H', 'N', 'H', 'N', 'N', 'H', 'N', 'H']
})

# Crear una tabla de contingencia
contingency_table = pd.crosstab(data['Deporte'], data['Sombrero'])

# Realizar un test de independencia (Chi-cuadrado)
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Comparar el p-valor con un nivel de significancia (por ejemplo, 0.05)
if p_value < 0.05:
    print("La posesión de un sombrero y jugar a un deporte NO son eventos independientes.")
else:
    print("La posesión de un sombrero y jugar a un deporte SON eventos independientes.")


"""
En este ejemplo, utilizamos la función pd.crosstab para crear una tabla de contingencia 
que muestra la frecuencia de las combinaciones de jugar fútbol o baloncesto y llevar 
puesto un sombrero o no. Luego, utilizamos el test de independencia Chi-cuadrado 
(chi2_contingency) para calcular el estadístico de prueba y el p-valor.

Si el p-valor es menor que un nivel de significancia predefinido (por ejemplo, 0.05), 
podemos concluir que la posesión de un sombrero y jugar a un deporte NO son eventos 
independientes. De lo contrario, si el p-valor es mayor que el nivel de significancia, 
podemos concluir que la posesión de un sombrero y jugar a un deporte SON eventos 
independientes.
"""