#Camberos Cordova Carlos Raul 20310415 6E2

import pygame
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

ANCHO = 800
ALTO = 600

def dibujar_grafo(grafo, aristas_seleccionadas, color_aristas):
    # Dibujar los nodos del grafo
    pos = nx.get_node_attributes(grafo, 'pos')
    nx.draw_networkx_nodes(grafo, pos, node_size=500, node_color='lightblue', alpha=0.9)

    # Dibujar las aristas del grafo
    nx.draw_networkx_edges(grafo, pos, alpha=0.7, edge_color='black', width=2)

    # Dibujar las aristas seleccionadas en rojo
    nx.draw_networkx_edges(grafo, pos, edgelist=aristas_seleccionadas, edge_color=color_aristas, width=2)

    # Dibujar las etiquetas de los nodos
    nx.draw_networkx_labels(grafo, pos, font_size=20, font_family='sans-serif')

    # Establecer los límites del eje
    plt.xlim([-1.2,1.2])
    plt.ylim([-1.2,1.2])

    # Actualizar la pantalla
    plt.pause(0.001)
    plt.show()
  

def crear_grafo(n):
    grafo = nx.Graph()

    # Crear los nodos
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        grafo.add_node(i, pos=(x, y))

    # Crear las aristas
    combinaciones = itertools.combinations(grafo.nodes(), 2)
    for u, v in combinaciones:
        if random.random() < 0.5:
            continue
        pos1 = grafo.nodes[u]['pos']
        pos2 = grafo.nodes[v]['pos']
        peso = random.randint(1, 20)
        grafo.add_edge(u, v, weight=peso, pos1=pos1, pos2=pos2)

    return grafo

# Función para encontrar el padre de un nodo en el algoritmo de Kruskal
def encontrar_padre(padres, nodo):
    if padres[nodo] != nodo:
        padres[nodo] = encontrar_padre(padres, padres[nodo])
    return padres[nodo]

# Función para unir dos componentes conexas en el grafo
def unir_componentes(padres, rank, nodo1, nodo2):
    padre1 = encontrar_padre(padres, nodo1)
    padre2 = encontrar_padre(padres, nodo2)
    if rank[padre1] > rank[padre2]:
        padres[padre2] = padre1
    else:
        padres[padre1] = padre2
        if rank[padre1] == rank[padre2]:
            rank[padre2] += 1

# Función para ordenar las aristas por peso
def ordenar_aristas_por_peso(aristas):
    return sorted(aristas, key=lambda x: x[2])

def kruskal_minimo_costo(grafo):
    # Inicializar los padres y los rangos de los nodos
    padres = {nodo: nodo for nodo in grafo.nodes()}
    rank = {nodo: 0 for nodo in grafo.nodes()}
    
    # Obtener las aristas del grafo y ordenarlas por peso
    aristas = [(u, v, data['weight']) for u, v, data in grafo.edges(data=True)]
    aristas_ordenadas = ordenar_aristas_por_peso(aristas)

    # Inicializar la lista de aristas seleccionadas y el peso total del árbol
    aristas_seleccionadas = []
    peso_total = 0
    
    # Seleccionar las aristas del árbol de mínimo costo
    for u, v, peso in aristas_ordenadas:
        if encontrar_padre(padres, u) != encontrar_padre(padres, v):
            aristas_seleccionadas.append((u, v))
            peso_total += peso
            unir_componentes(padres, rank, u, v)

            # Dibujar el grafo con las aristas seleccionadas
            dibujar_grafo(grafo, aristas_seleccionadas, 'r')

    # Imprimir el peso total del árbol de mínimo costo
    print(f'Peso total del árbol de mínimo costo: {peso_total}')
    
def kruskal_maximo_costo(grafo):
    # Inicializar los padres y los rangos de los nodos
    padres = {nodo: nodo for nodo in grafo.nodes()}
    rank = {nodo: 0 for nodo in grafo.nodes()}
    
    # Obtener las aristas del grafo y ordenarlas por peso de mayor a menor
    aristas = [(u, v, data['weight']) for u, v, data in grafo.edges(data=True)]
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2], reverse=True)
    
    # Verificar si hay al menos una arista con costo mayor a cero
    if len(aristas_ordenadas) == 0 or aristas_ordenadas[0][2] == 0:
        print('El grafo no tiene aristas con costo mayor a cero')
        return
    
    # Inicializar la lista de aristas seleccionadas y el peso total del árbol
    aristas_seleccionadas = []
    peso_total = 0
    
    # Seleccionar las aristas del árbol de máximo costo
    for u, v, peso in aristas_ordenadas:
        if encontrar_padre(padres, u) != encontrar_padre(padres, v):
            aristas_seleccionadas.append((u, v))
            peso_total += peso
            unir_componentes(padres, rank, u, v)

            # Dibujar el grafo con las aristas seleccionadas
            dibujar_grafo(grafo, aristas_seleccionadas, 'b')

    # Imprimir el peso total del árbol de máximo costo
    print(f'Peso total del árbol de máximo costo: {peso_total}')
    
def main():
    # Crear el grafo
    grafo = crear_grafo(10)
    # Dibujar el grafo vacío
    plt.figure(figsize=(8, 6))
    plt.axis('off')
    dibujar_grafo(grafo, [], 'none')

    # Ejecutar el algoritmo de Kruskal para encontrar el árbol de mínimo costo
    kruskal_minimo_costo(grafo)
    
    # Ejecutar el algoritmo de Kruskal para encontrar el árbol de máximo costo
    kruskal_maximo_costo(grafo)

    # Mostrar la ventana con la animación
    plt.show()

if __name__ == "__main__":
    main()
    
        