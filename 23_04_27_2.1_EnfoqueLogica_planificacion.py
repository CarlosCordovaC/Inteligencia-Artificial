# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:45:06 2023

@author: carlo

Un ejemplo cotidiano de la planificación con enfoque hacia la lógica es la planificación 
de una ruta de viaje. Para planificar una ruta, se deben considerar varios factores, como 
la distancia, el tiempo de viaje, el tráfico, las restricciones de velocidad, entre otros. 
Para lograr esto, se utiliza el conocimiento sobre la geografía y las restricciones de 
tráfico, junto con las reglas lógicas que definen cómo se pueden combinar las acciones 
para alcanzar el objetivo de llegar a un destino específico. De esta manera, se puede 
utilizar un algoritmo de planificación lógica para generar una ruta óptima que tenga en 
cuenta estos factores y permita llegar al destino en el menor tiempo posible.

planificación
"""
# Definir los predicados lógicos
def luz_encendida(estado):
    return estado["luz_comedor"] == "encendida"

def luz_apagada(estado):
    return estado["luz_comedor"] == "apagada"

def puerta_abierta(estado):
    return estado["puerta_garaje"] == "abierta"

def puerta_cerrada(estado):
    return estado["puerta_garaje"] == "cerrada"

def basura_sacada(estado):
    return estado["basura"] == "sacada"

# Definir las acciones disponibles
def encender_luz_comedor(estado):
    if luz_apagada(estado):
        estado["luz_comedor"] = "encendida"
        return estado
    else:
        return False

def abrir_puerta_garaje(estado):
    if puerta_cerrada(estado):
        estado["puerta_garaje"] = "abierta"
        return estado
    else:
        return False

def sacar_basura(estado):
    if puerta_abierta(estado) and not basura_sacada(estado):
        estado["basura"] = "sacada"
        return estado
    else:
        return False

def cerrar_puerta_garaje(estado):
    if puerta_abierta(estado):
        estado["puerta_garaje"] = "cerrada"
        return estado
    else:
        return False

def apagar_luz_comedor(estado):
    if luz_encendida(estado):
        estado["luz_comedor"] = "apagada"
        return estado
    else:
        return False

# Definir las reglas para la planificación
reglas = [
    (encender_luz_comedor, [luz_apagada]),
    (abrir_puerta_garaje, [puerta_cerrada]),
    (sacar_basura, [puerta_abierta, lambda estado: not basura_sacada(estado)]),
    (cerrar_puerta_garaje, [puerta_abierta]),
    (apagar_luz_comedor, [luz_encendida])
]

# Definir la función que verifica si un objetivo es alcanzable
def es_objetivo_alcanzable(estado, objetivo):
    for accion, precondiciones in objetivo:
        if not all(p(estado) for p in precondiciones):
            return False
    return True

# Definir la función
def planificar(estado_inicial, objetivo):
# Verificar si el objetivo es alcanzable
    if not es_objetivo_alcanzable(estado_inicial, objetivo):
        return False
    
estado_inicial = {"luz_comedor": "apagada", "puerta_garaje": "cerrada", "basura": "no sacada"}
objetivo = [(encender_luz_comedor, [luz_apagada]), (sacar_basura, [puerta_abierta, lambda estado: not basura_sacada(estado)]), (cerrar_puerta_garaje, [puerta_abierta])]
plan = planificar(estado_inicial, objetivo)
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print("-", accion.name)
else:
    print("No se pudo encontrar un plan que alcance el objetivo.")
