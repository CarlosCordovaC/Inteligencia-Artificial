#Utilidad y Toma de Decisiones 

# Definición del grafo de la ciudad
ciudad = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'E': 1, 'F': 4},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

# Función para encontrar la ruta más corta usando BFS
def bfs_camino_mas_corto(ciudad, origen, destino):
    # Creamos una cola para guardar los nodos que vamos a explorar
    cola = [(origen, [origen])]
    
    while cola:
        # Sacamos el primer nodo de la cola
        (nodo, camino) = cola.pop(0)
        
        # Si encontramos el destino, retornamos el camino
        if nodo == destino:
            return camino
        
        # Si no hemos encontrado el destino, seguimos explorando
        for vecino in ciudad[nodo]:
            if vecino not in camino:
                cola.append((vecino, camino + [vecino]))
    
    # Si no encontramos el destino, retornamos None
    return None

# Encontrar la ruta más corta de A a G
ruta_mas_corta = bfs_camino_mas_corto(ciudad, 'A', 'G')
print('La ruta más corta es:', ruta_mas_corta)
