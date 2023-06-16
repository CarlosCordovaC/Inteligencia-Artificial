import serial

# Configuración del puerto serie
port = "COM5"  # Cambia esto al puerto serie que desees utilizar
baudrate = 9600  # Velocidad de transmisión en baudios

# Inicializar el objeto Serial
ser = serial.Serial(port, baudrate)

# Función para encender o apagar el LED
def controlar_led(estado):
    if estado == "0":
        ser.write(b'0')  # Enviar '0' al Arduino para apagar el LED
        print("LED apagado")
    elif estado == "1":
        ser.write(b'1')  # Enviar '1' al Arduino para encender el LED
        print("LED encendido")
    else:
        print("Entrada inválida. Ingresa '0' para apagar el LED o '1' para encenderlo.")

# Loop principal
while True:
    # Solicitar al usuario ingresar el estado del LED
    entrada = input("Ingresa '0' para apagar el LED o '1' para encenderlo: ")
    
    # Controlar el LED según la entrada del usuario
    controlar_led(entrada)

# Cerrar el puerto serie (no se alcanzará esta línea mientras se ejecute el bucle infinito)
ser.close()
