dato = input("Ingresa el nombre de un superheroe :")

superheroe= ["ironman","hulk","spiderman","batman","flash"]

if dato in superheroe:
    print("El superheroe que agregaste ya esta en la lista: ",superheroe )
else:
    print ("El superheroe que agregaste no esta en la lista")
    
    
print("")
print("Ejercicio Python")
print("")

color = input("Ingresa un color: ")
coloresT = ("Rojo", "Azul", "Negro", "Cafe")

if color in coloresT :
    print ("El color ",color, "esta admitido")
else:
    print ("El color ",color, " no esta admitido")