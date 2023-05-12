# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:53 2023

@author: carlo

En resumen, la Red Bayesiana es una representación gráfica que permite modelar y 
realizar inferencias sobre situaciones inciertas y dependientes, utilizando las 
probabilidades condicionales y el Teorema de Bayes.
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear la estructura de la Red Bayesiana
model = BayesianModel([('Hum_Aire', 'Lluvia'), ('Viento', 'Lluvia')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_hum_aire = TabularCPD('Hum_Aire', 2, [[0.8, 0.2]])
cpd_viento = TabularCPD('Viento', 2, [[0.6, 0.4]])
cpd_lluvia = TabularCPD('Lluvia', 2, [[0.9, 0.7, 0.3, 0.1],
                                      [0.1, 0.3, 0.7, 0.9]],
                        evidence=['Hum_Aire', 'Viento'], evidence_card=[2, 2])

# Agregar los CPDs al modelo
model.add_cpds(cpd_hum_aire, cpd_viento, cpd_lluvia)

# Crear un objeto VariableElimination para realizar inferencias
inference = VariableElimination(model)

# Calcular la probabilidad condicional de lluvia dada la humedad del aire alta y el viento débil
query = inference.query(['Lluvia'], evidence={'Hum_Aire': 1, 'Viento': 0})
print(query['Lluvia'].values)
