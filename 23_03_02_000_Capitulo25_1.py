print ("Hola jugador selecciona tus mejoras: \n"+
       "abilidades de personaje: \n\n" +
       "Golpe: \n\n"
       "1.-Nivel1.......1 Punto\n" +
       "2.-Nivel2.......2 Puntos\n\n"+
       "Escudo: \n\n"
       "3.-Nivle.......1 Punto\n"+
       "4.-Nivel2......2 Puntos")

habilidades = [2]
puntos = 3

golpen1 = 1
golpen2 = 2

escudon1 = 1
escudon2 = 2


if 1 in habilidades:
    puntos = golpen1 - puntos
    print("Se a agregado Golpe Nivel 1 en tu inventario")

if 2 in habilidades:
    puntos = golpen2 - puntos
    print("Se a agregado Golpe Nivel 2 en tu inventario")

if 3 in habilidades:
    puntos = escudon1 - puntos
    print("Se a agregado Escudo Nivel 1 en tu inventario")

if 4 in habilidades:
    puntos = escudon2 - puntos
    print("Se a agregado Escudo Nivel 2 en tu inventario")
    
if puntos > 0:
    print("Necesitas mas puntos para esta compra ")

