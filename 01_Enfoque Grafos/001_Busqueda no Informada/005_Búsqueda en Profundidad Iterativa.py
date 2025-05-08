def busqueda_profundidad_iterativa(grafo, nodo_inicial, objetivo):
    profundidad = 0
    while True:
        resultado = busqueda_profundidad_limitada(grafo, nodo_inicial, objetivo, profundidad)
        if resultado:
            return resultado  # Retorna el camino si se encontró
        profundidad += 1  # Incrementa el límite de profundidad
