# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:14:02 2023

@author: carlo

Reconocimiento del Habla
"""

import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
recognizer = sr.Recognizer()

# Definir el archivo de audio a reconocer
archivo_audio = "audio.wav"

# Cargar el archivo de audio
with sr.AudioFile(archivo_audio) as source:
    # Leer el audio desde el archivo
    audio = recognizer.record(source)

    try:
        # Utilizar el reconocedor de voz para transcribir el audio
        texto_transcrito = recognizer.recognize_google(audio, language="es-ES")

        # Imprimir el texto transcrito
        print("Texto transcrito: ", texto_transcrito)

    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")

    except sr.RequestError as e:
        print("Error al solicitar el servicio de reconocimiento de voz; {0}".format(e))
