# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:31:27 2023

@author: carlo

Un ejemplo de cómo estas ramas de la lógica se pueden aplicar en la vida diaria es en 
el diseño de sistemas de seguridad para el hogar. Supongamos que deseamos diseñar un 
sistema de seguridad que se active automáticamente cuando se detecta la presencia de un 
intruso en nuestra casa. Podríamos utilizar la lógica modal para representar el 
conocimiento de nuestro sistema sobre el entorno en el que se mueve, y para tomar 
decisiones sobre qué acciones tomar en función de ese conocimiento. Podríamos utilizar 
la lógica temporal para modelar el comportamiento del sistema a lo largo del tiempo y 
para generar planes de acción que logren los objetivos deseados en un período de tiempo 
determinado. Finalmente, podríamos utilizar la lógica difusa para controlar variables 
como la intensidad de la luz, el nivel de ruido y la temperatura, y para tomar decisiones 
en función de las mediciones obtenidas por los sensores.


Lógicas Modal, Temporal y Difusa
"""
# Lógica modal
class ModalLogic:
    def __init__(self, worlds, relations):
        self.worlds = worlds
        self.relations = relations
    
    def validate(self, proposition):
        for world in self.worlds:
            if proposition.evaluate(world) and not self.check_relations(world):
                return False
        return True
    
    def check_relations(self, world):
        for relation in self.relations:
            if relation[0] == world and relation[1] not in self.worlds:
                return False
        return True

# Lógica temporal
class TemporalLogic:
    def __init__(self, worlds, relations):
        self.worlds = worlds
        self.relations = relations
    
    def validate(self, proposition, time):
        for world in self.worlds:
            if proposition.evaluate(world, time) and not self.check_relations(world, time):
                return False
        return True
    
    def check_relations(self, world, time):
        for relation in self.relations:
            if relation[0] == world and relation[1][0] <= time and relation[1][1] >= time and relation[2] not in self.worlds:
                return False
        return True

# Lógica difusa
class FuzzyLogic:
    def __init__(self, rules):
        self.rules = rules
    
    def infer(self, inputs):
        output = {}
        for rule in self.rules:
            strength = min([rule[input_name].fuzzify(inputs[input_name]) for input_name in inputs])
            for output_name in rule['output']:
                if output_name not in output:
                    output[output_name] = rule['output'][output_name].defuzzify(strength)
                else:
                    output[output_name] = max(output[output_name], rule['output'][output_name].defuzzify(strength))
        return output
