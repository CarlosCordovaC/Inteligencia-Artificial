# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:37:52 2023

@author: carlo

Supongamos que estás planeando una fiesta en tu casa y quieres decidir si debes hacerla en 
el jardín o en el salón, teniendo en cuenta el clima y tus preferencias personales. Puedes 
utilizar una Red de Decisión para modelar esta situación.

En la red, tendrías dos nodos de decisión: "Hacer la fiesta en el jardín" y "Hacer la fiesta 
en el salón". También tendrías un nodo de probabilidad llamado "Clima" con dos estados 
posibles: "Buen clima" y "Mal clima". Finalmente, tendrías un nodo de utilidad que representa 
la utilidad asociada a cada opción (por ejemplo, la comodidad, la facilidad de limpieza, etc.).

A través de la red, puedes asignar probabilidades a los estados del nodo 
Clima" y calcular la utilidad esperada para cada opción (hacer la fiesta en el 
jardín o en el salón) en función de las probabilidades y los valores de utilidad asignados.

De esta manera, puedes tomar una decisión informada sobre dónde realizar la fiesta 
en función de tus preferencias y las probabilidades del clima. La Red de Decisión te 
ayudará a evaluar las opciones y seleccionar la que maximice tu utilidad esperada.
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Creamos el modelo de la Red de Decisión
modelo = BayesianModel([('Clima', 'Ubicacion'), ('Preferencias', 'Ubicacion')])

# Definimos las distribuciones de probabilidad condicional (CPDs)
cpd_clima = TabularCPD(variable='Clima', variable_card=2, values=[[0.7, 0.3]])
cpd_preferencias = TabularCPD(variable='Preferencias', variable_card=2, values=[[0.6, 0.4]])
cpd_ubicacion = TabularCPD(variable='Ubicacion', variable_card=2,
                           evidence=['Clima', 'Preferencias'], evidence_card=[2, 2],
                           values=[[0.9, 0.6, 0.4, 0.1],
                                   [0.1, 0.4, 0.6, 0.9]])

# Asignamos los CPDs al modelo
modelo.add_cpds(cpd_clima, cpd_preferencias, cpd_ubicacion)

# Verificamos la consistencia del modelo
print("El modelo es consistente:", modelo.check_model())

# Realizamos una consulta para obtener la ubicación óptima en función del clima y las preferencias
inferencia = modelo.query(variables=['Ubicacion'], evidence={'Clima': 0, 'Preferencias': 1})
print("La ubicación óptima es:", inferencia['Ubicacion'].values[0])


"""
En este ejemplo, creamos una Red de Decisión con tres nodos: "Clima", 
"Preferencias" y "Ubicacion". El nodo "Clima" tiene dos estados posibles 
(0: Buen clima, 1: Mal clima), el nodo "Preferencias" también tiene dos estados posibles 
(0: No preferido, 1: Preferido), y el nodo "Ubicacion" representa las posibles ubicaciones 
para la fiesta (0: Jardín, 1: Salón).

Definimos las distribuciones de probabilidad condicional (CPDs) para cada nodo 
utilizando la clase TabularCPD de pgmpy. Estas distribuciones representan las 
probabilidades de transición entre los estados de los nodos.

Luego, agregamos los CPDs al modelo y verificamos su consistencia utilizando el 
método check_model(). Finalmente, realizamos una consulta al modelo para obtener 
la ubicación óptima en función del clima (Buen clima) y las preferencias (Preferido).
"""