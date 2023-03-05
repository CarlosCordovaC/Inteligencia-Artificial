teclado2 = {
        
   "Categoria": "Teclado",
   "Modelo": "Hyper X",
   "Precio": "950$"
        
   }
#Contar los elementos que tiene el diccionario teclado2
print(len(teclado2))

#Agregar una nueva variable
teclado2["Color"] = "Negro"

#Con esto hacemos una copia de nuestro diccionario teclado2
tecladocopia = teclado2.copy()

#Eliminar un dato del Diccionario teclado
teclado2.pop("Precio")



print(teclado2)
print(tecladocopia)

#Creacion de nuevos diccionarios con la funcion dict
teclado3 = dict(Categoria = "Tablets",
                Modelo = "Lenovo",
                Precio = "15,000",
                Almacenamiento = 200)

print(teclado3)


#Creacion de un diccionario de otra forma
teclado4 = ("Categoria","Almacenamiento","Precio")
vacio = "Sin valor"

teclado4 = dict.fromkeys(teclado4,vacio)
print(teclado4)

#Agregar un nuevo dato con la funcion update
teclado4.update({"Precio":"100$"})
print(teclado4)


#Utilizar la funcion if 

if "Precio" in teclado4:
    print("El producto tiene un precio")
else:
    print("Se necesita agregar un precio a este producto")


#De esta forma puedes anidar varios diccionarios

agencia = {
"auto":{
        "Modelo": "Tesla",
        "Año": "2023",
        "Motor": "Electrico"
        },

"auto1":{
        "Modelo": "Mercedez",
        "Año": "2023",
        "Motor": "Electrico"
        }
}
print(agencia)


print("Ejersisios de python\n")

#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves
#'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.

teclados1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclados2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclados1
teclados2.pop("Categoria","Precio")
print(teclados2['Modelo'])










