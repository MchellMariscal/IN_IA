from collections import deque

def verificar_cruce(camino_inicial, camino_objetivo):
    # Revisa si hay algún nodo común en los caminos
    for nodo in camino_inicial:
        if nodo in camino_objetivo:
            return nodo
    return None

def reconstruir_camino(camino, nodo_comun):
    # Reconstruye el camino desde el nodo hasta el nodo común
    camino_reconstruido = []
    nodo = nodo_comun
    while nodo is not None:
        camino_reconstruido.append(nodo)
        nodo = camino[nodo]
    return camino_reconstruido[::-1]  # Invertimos el camino

def busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo):
    if nodo_inicial == nodo_objetivo:
        return [nodo_inicial]
    
    # Inicializamos las fronteras de las dos búsquedas
    frontera_inicial = deque([nodo_inicial])
    frontera_objetivo = deque([nodo_objetivo])
    
    # Inicializamos los caminos desde el nodo inicial y objetivo
    camino_inicial = {nodo_inicial: None}
    camino_objetivo = {nodo_objetivo: None}
    
    while frontera_inicial and frontera_objetivo:
        # Expande un nodo de la frontera inicial
        nodo_actual_inicial = frontera_inicial.popleft()
        for vecino in grafo.get(nodo_actual_inicial, []):
            if vecino not in camino_inicial:
                camino_inicial[vecino] = nodo_actual_inicial
                frontera_inicial.append(vecino)

        # Expande un nodo de la frontera objetivo
        nodo_actual_objetivo = frontera_objetivo.popleft()
        for vecino in grafo.get(nodo_actual_objetivo, []):
            if vecino not in camino_objetivo:
                camino_objetivo[vecino] = nodo_actual_objetivo
                frontera_objetivo.append(vecino)

        # Verifica si las fronteras se cruzan
        nodo_comun = verificar_cruce(camino_inicial, camino_objetivo)
        if nodo_comun:
            # Si se cruzan, reconstruye el camino
            camino = reconstruir_camino(camino_inicial, nodo_comun) + reconstruir_camino(camino_objetivo, nodo_comun)[1:]
            return camino

    return None  # Si no se encuentra el camino

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

# Prueba de la Búsqueda Bidireccional
resultado = busqueda_bidireccional(grafo, 'A', 'G')
print(f'Ruta encontrada: {resultado}')
