import heapq

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

# Definimos una heurística simple (por ejemplo, la distancia Manhattan entre los nodos)
# En este caso, la heurística es solo un valor simulado que representa una estimación
heuristicas = {
    'A': 5,  # Heurística de A
    'B': 4,  # Heurística de B
    'C': 2,  # Heurística de C
    'D': 1,  # Heurística de D
    'E': 3,  # Heurística de E
    'F': 1,  # Heurística de F
    'G': 0   # Heurística de G (objetivo)
}

# Función heurística
def heuristica(nodo):
    return heuristicas.get(nodo, float('inf'))

# Búsqueda Voraz
def busqueda_voraz(grafo, nodo_inicial, nodo_objetivo, heuristica):
    open_list = []
    heapq.heappush(open_list, (heuristica(nodo_inicial), nodo_inicial))

    came_from = {}

    while open_list:
        _, nodo_actual = heapq.heappop(open_list)

        if nodo_actual == nodo_objetivo:
            # Reconstruir el camino
            camino = []
            while nodo_actual in came_from:
                camino.append(nodo_actual)
                nodo_actual = came_from[nodo_actual]
            camino.append(nodo_inicial)
            return camino[::-1]

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in came_from:  # Evitar ciclos
                came_from[vecino] = nodo_actual
                heapq.heappush(open_list, (heuristica(vecino), vecino))

    return None  # Si no se encuentra el objetivo

# Ejecutamos la Búsqueda Voraz para encontrar el camino desde A hasta G
camino = busqueda_voraz(grafo, 'A', 'G', heuristica)
print(f'Camino encontrado con Búsqueda Voraz: {camino}')

# Ejemplo de aplicación real: En la planificación de rutas de entrega, la búsqueda voraz puede ser utilizada para encontrar la ruta más corta entre múltiples puntos de entrega, optimizando el tiempo y los recursos.
