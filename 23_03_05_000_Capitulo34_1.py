print("Familia Simpson")

def familiaS(nombre,parentesco):
    print(nombre + " Simpson" + " "+ parentesco)

familiaS("Homero","Padre")
familiaS("Marge", "Madre")
familiaS("Bart", "Hijo y Hermano")
familiaS("Lisa", "Hija y Hermana")
familiaS("Maggie", "Hija y Hermana")

print("Ejersisios de python\n")
#Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos 
#(numero1 y numero2). En su interior, especificarás un print() que muestre el resultado 
#de la suma. Deberás hacer tres llamadas que como resultado de la suma den los valores 
#30, 50 y 57000. Los números que introduzcas en la llamada pueden ser los que quieras 
#siempre que coincidan los resultados en el print().

print("Funcion Suma")
def suma(numero1,numero2):
    print(numero1+numero2,"\n")
    
suma(15,15)
suma(25,25)
suma(5000,700)