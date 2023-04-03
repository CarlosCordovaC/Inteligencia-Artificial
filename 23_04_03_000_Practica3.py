#Camberos Cordova Carlos Raul 20310415 6E2 

import sys
import tkinter as tk

# Definimos una función que encuentre el vértice con la distancia mínima
def encontrar_minimo(distancia, visitado, vertices):
    minimo = sys.maxsize
    for v in vertices:
        if distancia[v] < minimo and visitado[v] == False:
            minimo = distancia[v]
            nodo_minimo = v
    return nodo_minimo

# Definimos la función que realiza el algoritmo de Dijkstra
def dijkstra(grafo, inicio, final, canvas):
    vertices = list(grafo.keys())
    distancia = {}
    previo = {}
    visitado = {}

    # Inicializamos los valores de distancia, previo y visitado
    for v in vertices:
        distancia[v] = sys.maxsize
        previo[v] = None
        visitado[v] = False

    # El vértice de inicio tiene distancia cero
    distancia[inicio] = 0

    # Bucle principal
    for i in range(len(vertices)):
        nodo_actual = encontrar_minimo(distancia, visitado, vertices)
        visitado[nodo_actual] = True

        # Actualizamos las distancias de los nodos adyacentes
        for nodo_adyacente, peso in grafo[nodo_actual].items():
            if visitado[nodo_adyacente] == False:
                nueva_distancia = distancia[nodo_actual] + peso
                if nueva_distancia < distancia[nodo_adyacente]:
                    distancia[nodo_adyacente] = nueva_distancia
                    previo[nodo_adyacente] = nodo_actual

        # Mostramos el estado actual del algoritmo en la interfaz gráfica
        canvas.itemconfigure(distancia_text, text=f"Distancias: {distancia}")
        canvas.itemconfigure(visitado_text, text=f"Visitado: {visitado}")
        canvas.itemconfigure(previo_text, text=f"Previo: {previo}")
        canvas.update()

    # Construimos el camino desde el nodo final al nodo inicial
    camino = []
    nodo = final
    while nodo != None:
        camino.insert(0, nodo)
        nodo = previo[nodo]

    # Mostramos el resultado final en la interfaz gráfica
    canvas.itemconfigure(resultado_text, text=f"El camino más corto desde {inicio} hasta {final} es: {camino}")
    canvas.itemconfigure(distancia_final_text, text=f"La distancia total es: {distancia[final]}")
    canvas.update()

# Función que se ejecuta cuando se presiona el botón "Calcular"
def calcular():
    grafo = {
        'A': {'B': 3, 'C': 2},
        'B': {'D': 2},
        'C': {'B': 1, 'D': 4},
        'D': {}
    }
    inicio = nodo_inicio.get()
    final = nodo_final.get()

    dijkstra(grafo, inicio, final, canvas)

# Creamos la interfaz gráfica
ventana = tk.Tk()
ventana.title("Algoritmo de Dijkstra")

# Creamos los widgets de la interfaz gráfica
titulo = tk.Label(ventana, text="Algoritmo de Dijkstra", font=("Arial", 20))
titulo.pack(pady=10)

canvas = tk.Canvas(ventana, width=600, height=200)
canvas.pack()

distancia_text = canvas.create_text(50, 50, text="Distancias: ", anchor="w")
visitado_text = canvas.create_text(50, 70, text="Visitado: ", anchor="w")
previo_text = canvas.create_text(50, 90, text="Previo: ", anchor="w")
resultado_text = canvas.create_text(50, 120, text="Resultado: ", anchor="w")
distancia_final_text = canvas.create_text(50, 140, text="Distancia total: ", anchor="w")

nodo_inicio_label = tk.Label(ventana, text="Nodo inicial:")
nodo_inicio_label.pack()
nodo_inicio = tk.Entry(ventana)
nodo_inicio.pack()

nodo_final_label = tk.Label(ventana, text="Nodo final:")
nodo_final_label.pack()
nodo_final = tk.Entry(ventana)
nodo_final.pack()

calcular_boton = tk.Button(ventana, text="Calcular", command=calcular)
calcular_boton.pack(pady=10)

ventana.mainloop()
