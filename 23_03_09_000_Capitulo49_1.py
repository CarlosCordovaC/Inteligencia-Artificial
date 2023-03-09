import re

texto= "Yo soy Iron Man - Tony Stark"
busqueda = re.split("soy",texto)
resultado = re.sub(" ","-",texto)



print(busqueda)
print(resultado)