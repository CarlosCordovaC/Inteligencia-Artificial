#Herencias en python
#La herencia me permite definir una clase
#que le da todos los metodos y propiedades de otra clase



class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre, self.edad)
        
usuario1 = Usuario("Julian", 56)
usuario1.muestra_datos()


#Sintaxis para crear una clase hijo
class Usuario_premium(Usuario):
    pass

usuario2 = Usuario_premium("Carlos", 21)
usuario2.muestra_datos()