
    
frase = "Lo que escribas lo repito: "
frase += '\n Introduce el comando "salir" para finalizar el programa \n'

mensaje = ""

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)


print("")
print("Ejercicio Python")
print("Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.\n")

a = 0
while a <= 15:
    print(a)
    a += 5

print("Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20")

b = 0
while b >= -100:
    print(b)
    b-=20


print("Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y "+
      "que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...")


c = 10
while c >= 0:
    print(c)
    c-=1