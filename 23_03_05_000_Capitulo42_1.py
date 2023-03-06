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
    def __init__(self, nombre, edad, instagram):
        #Con esta linea puedes ahorra codigo llamando la informacion de la clase padre, llamando solo la informacion que necesitas
        Usuario.__init__(self,nombre,edad)
        self.instagram = instagram
        
    def muestra_datos_premium(self):
        print("El nombre de usuario es: " + self.nombre, "y tiene", self.edad, "años. Su instagram es: ", self.instagram)

usuario2 = Usuario_premium("Carlos", 21, "Carlos_C_C")
usuario2.muestra_datos_premium()