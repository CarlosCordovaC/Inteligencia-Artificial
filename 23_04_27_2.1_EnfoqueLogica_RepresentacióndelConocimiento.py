# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:18:48 2023

@author: carlo

Un ejemplo de cómo se puede aplicar esta técnica en la vida diaria es mediante la 
creación de un sistema experto para la selección de alimentos saludables. En este 
caso, se puede utilizar la lógica para representar el conocimiento de un experto en 
nutrición, en términos de proposiciones y relaciones entre ellas. Por ejemplo, se pueden 
representar proposiciones como "las frutas son saludables", "las grasas saturadas son 
dañinas", "los alimentos procesados contienen muchos conservantes", entre otras.

Una vez que se ha representado el conocimiento, se pueden utilizar reglas lógicas para 
inferir si un alimento en particular es saludable o no. Por ejemplo, si se tiene la 
información de que una manzana es una fruta y que las frutas son saludables, se puede 
inferir que la manzana es saludable. De esta manera, se puede utilizar el sistema para 
recomendar alimentos saludables basados en la información proporcionada por el usuario.

Representación del Conocimiento
"""

class Animal:
    def __init__(self, especie, alimentacion, habitat):
        self.especie = especie
        self.alimentacion = alimentacion
        self.habitat = habitat

class Mamifero(Animal):
    def __init__(self, especie, alimentacion, habitat, gestacion):
        super().__init__(especie, alimentacion, habitat)
        self.gestacion = gestacion

class Perro(Mamifero):
    def __init__(self, especie, alimentacion, habitat, gestacion, raza):
        super().__init__(especie, alimentacion, habitat, gestacion)
        self.raza = raza

class Gato(Mamifero):
    def __init__(self, especie, alimentacion, habitat, gestacion, raza):
        super().__init__(especie, alimentacion, habitat, gestacion)
        self.raza = raza

class Pajaro(Animal):
    def __init__(self, especie, alimentacion, habitat, color):
        super().__init__(especie, alimentacion, habitat)
        self.color = color

perro1 = Perro("Canis lupus familiaris", "Carnívoro", "Terrestre", "63 días", "Chihuahua")
gato1 = Gato("Felis catus", "Carnívoro", "Terrestre", "64 - 67 días", "Persa")
pajaro1 = Pajaro("Parus major", "Omnívoro", "Aéreo", "Negro, blanco y gris")

print("El perro de raza", perro1.raza, "es un", perro1.especie, "que se alimenta de", perro1.alimentacion, "y habita en", perro1.habitat, "con un período de gestación de", perro1.gestacion)
print("El gato de raza", gato1.raza, "es un", gato1.especie, "que se alimenta de", gato1.alimentacion, "y habita en", gato1.habitat, "con un período de gestación de", gato1.gestacion)
print("El pájaro de especie", pajaro1.especie, "es un", pajaro1.habitat, "que se alimenta de forma", pajaro1.alimentacion, "y es de color", pajaro1.color)
