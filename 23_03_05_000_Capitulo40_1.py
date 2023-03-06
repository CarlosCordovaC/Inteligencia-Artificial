class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre, self.edad)
        
usuario1 = Usuario("Julian", 56)
usuario1.muestra_datos()



#Cambiar una propiedad 
usuario1.edad = 65
usuario1.muestra_datos()

#Eliminar una propiedad
del usuario1.edad
usuario1.muestra_datos()

#Para eliminar un objeto solo pon el nombre del objeto
#del usuario1