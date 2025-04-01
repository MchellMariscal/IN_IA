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

def busqueda_profundidad_iterativa(grafo, nodo_inicial, objetivo):
    profundidad = 0
    while True:
        # Llamamos a la Búsqueda en Profundidad Limitada con la profundidad actual
        resultado = busqueda_profundidad_limitada(grafo, nodo_inicial, objetivo, profundidad)
        if resultado:
            return resultado
        profundidad += 1  # Aumentamos la profundidad en cada iteración

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

# Prueba de la Búsqueda en Profundidad Iterativa
resultado = busqueda_profundidad_iterativa(grafo, 'A', 'G')
print(f'Ruta encontrada: {resultado}')
