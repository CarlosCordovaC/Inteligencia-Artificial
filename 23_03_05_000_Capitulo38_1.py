class Usuario:
    def __init__(self, nombre, pin):  
        self.nombre = nombre
        self.pin = pin         

    def saludo(self):
        print("Saludos " + self.nombre + " Inciaste sesion correctamente " )

    def despedida(self):
        print(" Gracias por su visita " , self.nombre , " Iniciate con tu pin " , self.pin)

usuario1 =Usuario("Carlos", 54321)
usuario2 =Usuario("Raul", 12345)

usuario1.saludo()
usuario2.despedida()