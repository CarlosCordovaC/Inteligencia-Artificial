# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:13:57 2023

@author: carlo

Filtrado, Predicción, Suavizado y Explicación

En resumen, el filtrado se centra en estimar el estado actual, la predicción en 
estimar el estado futuro, el suavizado en estimar el estado pasado y la explicación 
en proporcionar interpretaciones de las relaciones causales entre el estado oculto y 
las observaciones a lo largo del tiempo. Estos conceptos son fundamentales en el análisis 
y modelado de datos secuenciales en el campo de la inteligencia artificial.
"""

import numpy as np
from scipy.stats import norm

# Datos observados (flujo de tráfico)
observaciones = [50, 55, 60, 58, 62]

# Filtrado: Estimación en tiempo real del flujo de tráfico actual
media_previa = 50  # Valor inicial de la media
varianza_previa = 10  # Valor inicial de la varianza
for observacion in observaciones:
    # Actualizar la estimación utilizando el filtro de Kalman
    media_filtrada = (varianza_previa * observacion + media_previa * 10) / (varianza_previa + 10)
    varianza_filtrada = (varianza_previa * 10) / (varianza_previa + 10)
    
    # Actualizar los valores previos para la próxima iteración
    media_previa = media_filtrada
    varianza_previa = varianza_filtrada

# Predicción: Predecir el flujo de tráfico futuro
num_pasos = 3  # Número de pasos de predicción
media_prediccion = media_filtrada  # Utilizar la media filtrada como valor inicial
varianza_prediccion = varianza_filtrada  # Utilizar la varianza filtrada como valor inicial
predicciones = []
for _ in range(num_pasos):
    # Generar una muestra aleatoria de la distribución predictiva
    muestra = np.random.normal(media_prediccion, np.sqrt(varianza_prediccion))
    predicciones.append(muestra)
    
# Suavizado: Estimación retrospectiva del flujo de tráfico pasado
suavizado = []
for i in range(len(observaciones)):
    # Calcular la distribución suavizada utilizando el suavizado de Kalman
    media_suavizada = (varianza_filtrada * observaciones[i] + media_filtrada * 10) / (varianza_filtrada + 10)
    varianza_suavizada = (varianza_filtrada * 10) / (varianza_filtrada + 10)
    suavizado.append(media_suavizada)
    # Actualizar los valores filtrados para la siguiente iteración
    media_filtrada = media_suavizada
    varianza_filtrada = varianza_suavizada

# Explicación: Análisis de las causas subyacentes del flujo de tráfico
eventos_especiales = [0, 0, 1, 0, 0]  # Indicador de eventos especiales (0: no hay evento, 1: evento)
causas = ['Sin evento', 'Sin evento', 'Evento especial', 'Sin evento', 'Sin evento']
explicacion = zip(observaciones, causas)

# Imprimir resultados
print("Filtrado:", media_filtrada)
print("Predicciones:", predicciones)
print("Suavizado:", suavizado)
print("Explicación:")
for observacion, causa in explicacion:
    print(f"Observación: {observacion}, Causa: {causa}")
