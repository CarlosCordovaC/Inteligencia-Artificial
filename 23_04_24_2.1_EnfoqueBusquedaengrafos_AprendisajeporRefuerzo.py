grafo_entorno = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {'H'},
    'E': {'I'},
    'F': {'J'},
    'G': {'K'},
    'H': set(),
    'I': set(),
    'J': set(),
    'K': set()
}
def buscar_camino(start, goal, grafo_entorno):
    visitados = set()
    pila = [(start, 0, [])]
    
    while pila:
        (nodo_actual, recompensa, camino) = pila.pop()
        if nodo_actual == goal:
            camino.append(nodo_actual)
            return (camino, recompensa)
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for vecino in grafo_entorno[nodo_actual]:
                if vecino not in visitados:
                    pila.append((vecino, recompensa + 1, camino + [nodo_actual]))
    return ([], -1)
start = 'A'
goal = 'K'
num_iteraciones = 10

for i in range(num_iteraciones):
    (camino, recompensa) = buscar_camino(start, goal, grafo_entorno)
    print(f"Iteración {i}: Camino encontrado: {camino}, recompensa total: {recompensa}")
