# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:54:51 2023

@author: carlo

Un ejemplo de lógica proposicional en la vida cotidiana es el siguiente: 
    "Si llueve, entonces me quedo en casa". En esta proposición, "llueve" 
    es la premisa y "me quedo en casa" es la conclusión. Si en algún momento 
    se verifica que está lloviendo, entonces se puede inferir lógicamente que 
    la persona se quedará en casa. Este tipo de razonamiento lógico se utiliza 
    en muchos contextos, como en la toma de decisiones, la planificación, la robótica, 
    entre otros.
    

lógica proposicional

"""

# Definimos las proposiciones
p = True
q = False

# Negación
not_p = not p
print(f"La negación de p es {not_p}")  # False

# Conjunción
p_and_q = p and q
print(f"La conjunción de p y q es {p_and_q}")  # False

# Disyunción
p_or_q = p or q
print(f"La disyunción de p y q es {p_or_q}")  # True

# Implicación
p_implies_q = not p or q
print(f"La implicación de p a q es {p_implies_q}")  # True

# Doble implicación
p_iff_q = (not p or q) and (not q or p)
print(f"La doble implicación de p y q es {p_iff_q}")  # False


"""
En este ejemplo, se definen dos proposiciones simples p y q. Luego, se aplican operadores 
lógicos como la negación, la conjunción, la disyunción, la implicación y la doble implicación 
para realizar razonamientos sobre estas proposiciones.

Es importante tener en cuenta que la lógica proposicional es un tipo de lógica formal que 
se utiliza para representar proposiciones simples y realizar razonamientos sobre ellas. 
Aunque puede ser útil en algunos casos, su capacidad de representación es limitada y, en 
la práctica, se utilizan lógicas más complejas como la lógica de primer orden o la lógica
 modal para representar conocimiento y realizar razonamientos más sofisticados.
"""