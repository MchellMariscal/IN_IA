import random

# Grafo de ejemplo con valores heurísticos asociados a cada nodo
grafo = {
    'A': {'B': 3, 'C': 5},
    'B': {'A': 3, 'D': 7, 'E': 4},
    'C': {'A': 5, 'F': 6},
    'D': {'B': 7},
    'E': {'B': 4, 'G': 8},
    'F': {'C': 6},
    'G': {'E': 8}
}

# Heurística asociada a cada nodo
heuristica = {
    'A': 1,
    'B': 3,
    'C': 5,
    'D': 7,
    'E': 4,
    'F': 6,
    'G': 8  # Nodo con la mejor heurística (óptimo global)
}

def hill_climbing(grafo, nodo_inicial):
    nodo_actual = nodo_inicial
    camino = [nodo_actual]
    
    while True:
        vecinos = grafo.get(nodo_actual, {})
        
        # Elegimos el vecino con la mejor heurística
        mejor_vecino = None
        mejor_valor = heuristica[nodo_actual]
        
        for vecino in vecinos:
            if heuristica[vecino] > mejor_valor:
                mejor_vecino = vecino
                mejor_valor = heuristica[vecino]
        
        # Si no hay mejor vecino, terminamos
        if mejor_vecino is None:
            return camino
        
        nodo_actual = mejor_vecino
        camino.append(nodo_actual)

# Prueba con el nodo inicial 'A'
resultado = hill_climbing(grafo, 'A')
print(f'Camino encontrado con Ascensión de Colinas: {resultado}')
