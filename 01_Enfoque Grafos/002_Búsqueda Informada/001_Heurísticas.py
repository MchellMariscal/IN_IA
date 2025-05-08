import heapq

# Definimos el grafo con costos asociados a las aristas
grafo = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 3},
    'C': {'A': 3, 'F': 1},
    'D': {'B': 1},
    'E': {'B': 3, 'G': 1},
    'F': {'C': 1},
    'G': {'E': 1}
}

# Definimos una heurística simple (por ejemplo, distancia Euclidiana entre nodos)
# En este caso, solo simularemos la heurística con un diccionario simple
# (realmente dependería de las coordenadas o un modelo de estimación del problema).

# Asumimos que los nodos están en una línea (esto es solo un ejemplo).
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

# Función de costo de arista (si no se define, se asume infinito)
def costo_de(nodo1, nodo2):
    return grafo.get(nodo1, {}).get(nodo2, float('inf'))

# Ejemplo de aplicación real: En un sistema de navegación GPS, las heurísticas pueden ser usadas para estimar la distancia más corta entre dos puntos en un mapa, ayudando a guiar al usuario por la ruta más eficiente.
