def busqueda_profundidad_limitada(grafo, nodo_inicial, objetivo, profundidad_maxima):
    if nodo_inicial == objetivo:
        return [nodo_inicial]  # Objetivo encontrado

    if profundidad_maxima == 0:
        return None  # Límite alcanzado, detener búsqueda

    for vecino in grafo.get(nodo_inicial, []):  # Buscar en vecinos
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, profundidad_maxima - 1)
        if resultado:
            return [nodo_inicial] + resultado  # Agregar nodo al camino

    return None  # No se encontró
