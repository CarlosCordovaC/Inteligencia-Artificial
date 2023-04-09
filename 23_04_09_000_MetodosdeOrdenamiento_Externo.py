#Camberos Cordova Carlos Raul 20310415

import random
import os

# Función de mezcla para ordenamiento externo
def merge(left_file, right_file, output_file):
    with open(left_file, 'r') as left, open(right_file, 'r') as right, open(output_file, 'w') as output:
        left_line = left.readline()
        right_line = right.readline()

        while left_line and right_line:
            if int(left_line) < int(right_line):
                output.write(left_line)
                left_line = left.readline()
            else:
                output.write(right_line)
                right_line = right.readline()

        # Escribir el resto de las líneas del archivo izquierdo, si las hay
        while left_line:
            output.write(left_line)
            left_line = left.readline()

        # Escribir el resto de las líneas del archivo derecho, si las hay
        while right_line:
            output.write(right_line)
            right_line = right.readline()

# Función de ordenamiento externo con mezcla
def external_merge_sort(input_file, output_file, chunk_size=10):
    # Dividir el archivo de entrada en archivos más pequeños y ordenarlos en memoria
    with open(input_file, 'r') as input:
        chunk = []
        for line in input:
            chunk.append(line)
            if len(chunk) == chunk_size:
                chunk.sort()
                with open(f'temp_{random.random()}.txt', 'w') as temp:
                    temp.write(''.join(chunk))
                chunk = []
        if chunk:
            chunk.sort()
            with open(f'temp_{random.random()}.txt', 'w') as temp:
                temp.write(''.join(chunk))

    # Mezclar los archivos temporales en uno solo ordenado
    chunk_files = [f for f in os.listdir() if f.startswith('temp_')]
    while len(chunk_files) > 1:
        next_chunk_files = []
        for i in range(0, len(chunk_files), 2):
            if i+1 < len(chunk_files):
                merge(chunk_files[i], chunk_files[i+1], f'temp_{random.random()}.txt')
                next_chunk_files.append(f'temp_{random.random()}.txt')
            else:
                next_chunk_files.append(chunk_files[i])
        chunk_files = next_chunk_files

    # Escribir el archivo de salida ordenado
    os.rename(chunk_files[0], output_file)

    # Eliminar los archivos temporales
    for f in os.listdir():
        if f.startswith('temp_'):
            os.remove(f)

# Generar un archivo de entrada con números aleatorios
input_file = 'input.txt'
with open(input_file, 'w') as f:
    for i in range(10):
        f.write(str(random.randint(1, 100)) + '\n')

# Ordenar el archivo de entrada y guardar el resultado en un archivo de salida
output_file = 'output.txt'
external_merge_sort(input_file, output_file)

# Imprimir los primeros 10 números del archivo de salida para verificar el ordenamiento
with open(output_file, 'r') as f:
    for i in range(10):
        print(f.readline().strip())
