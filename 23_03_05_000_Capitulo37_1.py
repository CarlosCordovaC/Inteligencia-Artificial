class heroe():
    nombre = "Superman"
    peso = 150
    colorP = "Azul"
    poderesP = "Volar"
    npoderes = 4
    inmunidad = False
    superfuersa = True
    
    def poder(self):
        self.inmunidad=True
    
    def criptonita(self):
        self.superfuersa(False)

heroe.poder()
heroe.criptonita()