"""def funcion1():
    variable1 = "Variable dentro de la funcion"
    print(variable1)
    
    def funcion2():
        variable1 = "He cambiado el valor de la funcion"
        print(variable1)
        
    funcion2()
    
funcion1()"""

#.------------------------------------------------------------------
#Variables globales

"""variable1 = "Vairiable fuera de la funcion"
def funcion1():
    variable1 = "Variable dentro de la funcion"
    print(variable1)
    
funcion1()
print(variable1)"""

#.-------------------------------------------------------------------
#Hacer una variable local global
num1 = 50

def funcion1():
    global num1
    num1 = 10
    print(num1)
    
funcion1()
print(num1)
    