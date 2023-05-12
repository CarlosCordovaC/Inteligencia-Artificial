# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:06 2023

@author: carlo

Eliminación de Variables

La eliminación de variables se utiliza ampliamente en el razonamiento probabilístico, 
incluyendo métodos como la propagación hacia atrás, los algoritmos de inferencia aproximada 
y las redes bayesianas. Permite simplificar los cálculos y mejorar el rendimiento en la 
resolución de problemas probabilísticos complejos.
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Crear la red bayesiana
model = BayesianModel([('resfriado', 'fiebre'), ('resfriado', 'tos')])

# Definir las probabilidades condicionales
cpd_resfriado = TabularCPD('resfriado', 2, [[0.95], [0.05]])
cpd_fiebre = TabularCPD('fiebre', 2, [[0.2, 0.8], [0.8, 0.2]], evidence=['resfriado'], evidence_card=[2])
cpd_tos = TabularCPD('tos', 2, [[0.3, 0.7], [0.7, 0.3]], evidence=['resfriado'], evidence_card=[2])

# Añadir las probabilidades condicionales a la red
model.add_cpds(cpd_resfriado, cpd_fiebre, cpd_tos)

from pgmpy.inference import VariableElimination

# Crear un objeto VariableElimination
infer = VariableElimination(model)

# Calcular la probabilidad de tener resfriado dado que tenemos fiebre y tos
query = infer.query(variables=['resfriado'], evidence={'fiebre': 1, 'tos': 1})
print(query)
