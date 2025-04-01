from collections import deque

def bfs(grafo, nodo_inicial):
    # Cola para explorar los nodos
    cola = deque([nodo_inicial])
    # Conjunto para almacenar los nodos visitados
    visitados = set([nodo_inicial])
    
    # Lista para almacenar el camino
    camino = []
    
    while cola:
        nodo_actual = cola.popleft()
        camino.append(nodo_actual)
        
        # Recorrer los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                
    return camino

# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Prueba de BFS
resultado_bfs = bfs(grafo, 'A')
print(f'Recorriendo el grafo con BFS: {resultado_bfs}')
