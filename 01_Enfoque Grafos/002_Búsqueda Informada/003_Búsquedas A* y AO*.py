import heapq

# Grafo de ejemplo
grafo = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 3},
    'C': {'A': 3, 'F': 1},
    'D': {'B': 1},
    'E': {'B': 3, 'G': 1},
    'F': {'C': 1},
    'G': {'E': 1}
}

# Heurísticas de ejemplo (simuladas)
heuristicas = {
    'A': 5,  # Heurística de A
    'B': 4,  # Heurística de B
    'C': 2,  # Heurística de C
    'D': 1,  # Heurística de D
    'E': 3,  # Heurística de E
    'F': 1,  # Heurística de F
    'G': 0   # Heurística de G
}

def heuristica(nodo):
    return heuristicas.get(nodo, float('inf'))

def costo_de(nodo1, nodo2):
    return grafo.get(nodo1, {}).get(nodo2, float('inf'))

# Algoritmo A*
def a_star(grafo, nodo_inicial, nodo_objetivo, heuristica):
    abrir_lista = []
    heapq.heappush(abrir_lista, (heuristica(nodo_inicial), nodo_inicial))

    g = {nodo_inicial: 0}
    f = {nodo_inicial: heuristica(nodo_inicial)}
    came_from = {}

    while abrir_lista:
        _, nodo_actual = heapq.heappop(abrir_lista)

        if nodo_actual == nodo_objetivo:
            # Reconstruir el camino
            camino = []
            while nodo_actual in came_from:
                camino.append(nodo_actual)
                nodo_actual = came_from[nodo_actual]
            camino.append(nodo_inicial)
            return camino[::-1]

        for vecino, costo in grafo.get(nodo_actual, {}).items():
            tentative_g = g[nodo_actual] + costo
            if vecino not in g or tentative_g < g[vecino]:
                came_from[vecino] = nodo_actual
                g[vecino] = tentative_g
                f[vecino] = tentative_g + heuristica(vecino)
                heapq.heappush(abrir_lista, (f[vecino], vecino))

    return None  # Si no se encuentra el objetivo

# Ejecutar A* desde 'A' hasta 'G'
camino = a_star(grafo, 'A', 'G', heuristica)
print(f'Camino encontrado con A*: {camino}')

# Ejemplo de aplicación real: En la robótica, el algoritmo A* es utilizado para la navegación autónoma de robots en entornos desconocidos, permitiéndoles encontrar el camino más eficiente hacia un objetivo.
