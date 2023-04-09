#Camberos Cordova Carlos Raul 20310415 6E2
import random

# Algoritmos de ordenamiento interno
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generamos una lista de números aleatorios
num_list = [random.randint(1, 100) for _ in range(10)]

# Mostramos la lista antes de ordenar
print("Lista sin ordenar:")
print(num_list)

# Ordenamos la lista utilizando el algoritmo de inserción
insertion_sort(num_list)
print("Lista ordenada con el algoritmo de inserción:")
print(num_list)

# Generamos una nueva lista de números aleatorios
num_list = [random.randint(1, 100) for _ in range(10)]

# Mostramos la lista antes de ordenar
print("Lista sin ordenar:")
print(num_list)

# Ordenamos la lista utilizando el algoritmo de selección
selection_sort(num_list)
print("Lista ordenada con el algoritmo de selección:")
print(num_list)

# Generamos una nueva lista de números aleatorios
num_list = [random.randint(1, 100) for _ in range(10)]

# Mostramos la lista antes de ordenar
print("Lista sin ordenar:")
print(num_list)

# Ordenamos la lista utilizando el algoritmo de burbuja
bubble_sort(num_list)
print("Lista ordenada con el algoritmo de burbuja:")
print(num_list)
