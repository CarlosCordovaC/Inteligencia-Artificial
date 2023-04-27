# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:40:47 2023

@author: carlo


Un ejemplo de Red Bayesiana en la vida cotidiana podría ser un sistema de 
diagnóstico médico. Supongamos que una persona va al médico con síntomas de 
una enfermedad. El médico utiliza una Red Bayesiana para modelar las posibles 
causas de los síntomas y las relaciones entre ellos. Por ejemplo, el dolor de 
cabeza podría ser causado por la gripe o por una infección sinusal. 
El médico introduce la evidencia observada, como la fiebre y la duración de los 
síntomas, en la Red Bayesiana y utiliza el modelo para calcular la probabilidad 
de cada posible diagnóstico. En base a esta información, el médico puede tomar 
una decisión sobre el tratamiento más adecuado para la persona.


Razonamiento Probabilístico: Red Bayesiana
"""
# Definición de la red bayesiana
red_bayesiana = {
    'Dolor de cabeza': {
        'Probabilidad': 0.1,
        'Dependencias': ['Fiebre', 'Fatiga']
    },
    'Fiebre': {
        'Probabilidad': 0.05,
        'Dependencias': ['Gripe']
    },
    'Fatiga': {
        'Probabilidad': 0.2,
        'Dependencias': ['Gripe']
    },
    'Gripe': {
        'Probabilidad': 0.01,
        'Dependencias': []
    }
}

# Función para calcular la probabilidad conjunta de las variables
def calcular_probabilidad_conjunta(red_bayesiana, variables):
    probabilidad_total = 1.0
    for variable in variables:
        dependencias = red_bayesiana[variable]['Dependencias']
        if not dependencias:
            probabilidad_total *= red_bayesiana[variable]['Probabilidad']
        else:
            dependencia = dependencias[0]
            prob_dependencia = red_bayesiana[dependencia]['Probabilidad']
            prob_condicional = red_bayesiana[variable]['Probabilidad']
            if dependencia in variables:
                probabilidad_total *= prob_condicional
            else:
                probabilidad_total *= prob_condicional * prob_dependencia
    return probabilidad_total

# Ejemplo de cálculo de probabilidad
prob_gripe_fatiga = calcular_probabilidad_conjunta(red_bayesiana, ['Gripe', 'Fatiga'])
print(f'La probabilidad conjunta de tener gripe y fatiga es: {prob_gripe_fatiga}')
