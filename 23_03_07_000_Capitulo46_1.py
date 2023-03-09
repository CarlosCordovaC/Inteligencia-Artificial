import datetime,locale 
locale.setlocale(locale.LC_ALL,"es-ES")

fecha = datetime.datetime.now()
#Dia
print(fecha.strftime("%A"))
#Horas
print(fecha.strftime("%H"))
#Minutos
print(fecha.strftime("%M"))
#Mes
print(fecha.strftime("%B"),fecha.strftime("%b"))