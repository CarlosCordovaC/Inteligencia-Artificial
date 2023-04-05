#Camberos Cordova Carlos Raul 20310415
import heapq
import networkx as nx
import matplotlib.pyplot as plt


#La clase Arista define una arista en el grafo, con un destino y un peso.
class Arista:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
#La clase Grafo define un grafo, con una lista de vértices y una lista de aristas. 
class Grafo:
    def __init__(self):
        self.vertices = {}
#El método agregar_vertice agrega un vértice al grafo
    def agregar_vertice(self, v):
        self.vertices[v] = []

#mientras que agregar_arista agrega una arista con un peso determinado entre dos vértices.
    def agregar_arista(self, v1, v2, peso):
        self.vertices[v1].append((v2, peso))
        self.vertices[v2].append((v1, peso))


    
    def prim(grafo, inicio):
        arbol = set()
        visitados = set([inicio])
        cola = [(peso, inicio, v) for v, peso in grafo.vertices[inicio]]
        heapq.heapify(cola)
    
        print("Paso 1: Visitando vértice", inicio)
        
        while cola:
            peso, origen, destino = heapq.heappop(cola)
            if destino not in visitados:
                visitados.add(destino)
                arbol.add((origen, destino, peso))
                print(f"Paso {len(arbol)+1}: Agregando arista ({origen}, {destino}, {peso}) al árbol")
                for v, peso in grafo.vertices[destino]:
                    if v not in visitados:
                        heapq.heappush(cola, (peso, destino, v))
                        print(f"Paso {len(arbol)+1}: Agregando vértice {v} a la cola de prioridad con peso {peso}")
            else:
                print(f"Paso {len(arbol)+1}: Descartando arista ({origen}, {destino}, {peso}) porque el destino {destino} ya fue visitado")
    
        return arbol

# Ejemplo de uso
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_vertice('E')
g.agregar_arista('A', 'B', 2)
g.agregar_arista('A', 'C', 3)
g.agregar_arista('B', 'C', 1)
g.agregar_arista('B', 'D', 1)
g.agregar_arista('C', 'D', 2)
g.agregar_arista('C', 'E', 1)
g.agregar_arista('D', 'E', 3)
arbol = g.prim('A')
print("Árbol parcial mínimo de Prim:", arbol)

# Crear el grafo visual
G = nx.Graph()
for v in g.vertices.keys():
    G.add_node(v)
for a in arbol:
    G.add_edge(a[0], a[1], weight=a[2])
    
# Dibujar el grafo visual
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
