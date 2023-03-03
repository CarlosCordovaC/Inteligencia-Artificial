print("")
print("Ejercicio Python")
print("")
print("Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120")
print("")



edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >=18 and edad <=45:
    print("Estas en un rango de edad de 18 a 45")

elif edad >= 45 and edad <= 100:
	print('Eres mayor de edad.')
    
elif edad >=100 and edad <=120:
    print("Tienes un rango de edad de 100 a 120")
else:
	print('Edad no válida.')