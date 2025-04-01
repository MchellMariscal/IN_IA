def busqueda_profundidad_limitada(grafo, nodo_inicial, objetivo, profundidad_maxima):
    # Caso base: si el nodo inicial es el objetivo
    if nodo_inicial == objetivo:
        return [nodo_inicial]
    
    # Si hemos alcanzado la profundidad máxima, no buscamos más
    if profundidad_maxima == 0:
        return None
    
    # Si no hemos alcanzado el objetivo, seguimos buscando en los vecinos
    for vecino in grafo.get(nodo_inicial, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, profundidad_maxima - 1)
        if resultado:
            return [nodo_inicial] + resultado
    
    # Si no encontramos el objetivo, devolvemos None
    return None

# Prueba con el grafo dado
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Llamamos a la función con un límite de profundidad de 3
resultado = busqueda_profundidad_limitada(grafo, 'A', 'G', 3)
print(f'Ruta encontrada: {resultado}')
