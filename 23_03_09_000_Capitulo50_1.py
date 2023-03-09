import re

texto= "Bienvenidos a programacion 55"

#Usando la D lo que hace es que me muestra solo el texto sin el numero
busqueda = re.findall("\D",texto)

#Metacaracteres 
resultado = re.findall("Bien...idos",texto)
#Con este simbolo | podemos buscar tanto una palabra como la otra ejemplo:Bienvenidos|Bienvenidas
#Con este simbolo[a-p]podemos hacer que busque todas letras dentro de el




print(busqueda)
print(resultado)