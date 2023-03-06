def colores(**kwargs):
    print("Este es el color " + kwargs["color1"] + ".")
    
colores(color1 = "rojo", color2 = "azul", color3 = "amarillo" , color4 = "verde")


#--------------------------------------------------------------------------------------------------
def autos(solo = "falta auto"):
    print("Tu auto seleccionado fue: " + solo +".")

autos("Audi")
autos()
