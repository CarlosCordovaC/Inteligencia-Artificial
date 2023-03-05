#Argumentos arbitrarios
def alumnos(*args):
    print("El ultimo alumno es: " + args[3] +" El primer alumno es: " + args[0])
    
alumnos("Andres","Carlos","Alex","Raul")


def alumnos_profesores(profesor, sustituto, *args):
    print("Profesor " + profesor)
    print("Sustituto " + sustituto)
    for x in args:
        print("Alumno: " + x)

lista_alumnos=["Andres","Carlos","Alex","Raul"]
alumnos_profesores("Antonio", "Alejandro", *lista_alumnos)


print("Ejersisios de python\n")
#¿Cuántos argumentos se utilizan en cada una de estas llamadas?


def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')# 4 Argumentos
colores('lila', 'negro', 'rojo')#3 Argumentos
colores('rosa')#1 Arguemnto
colores('marrón', 'naranja')#2 Argumentos

#Completa el siguiente fragmento de código:
def colores(*args):
	print(" El color " + args[1] + " es mi favorito. " + " El color " + args[0]+ " tampoco está mal ")

colores("Rojo","Azul","Verde")

#Crea una función que realice la suma de cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*argsm):
    resultado = argsm[0]+argsm[1]+argsm[2]+argsm[3]+argsm[4]
    print("El resultado de la suma es: ", resultado)

suma(1,1,1,1,1)



