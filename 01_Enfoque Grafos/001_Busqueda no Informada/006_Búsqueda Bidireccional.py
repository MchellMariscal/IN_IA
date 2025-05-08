from collections import deque  # Importamos deque para usar colas eficientes

# Verifica si hay algún nodo en común entre las dos búsquedas
def verificar_cruce(camino_inicial, camino_objetivo):
    for nodo in camino_inicial:
        if nodo in camino_objetivo:
            return nodo  # Nodo donde se cruzan las búsquedas
    return None

# Reconstruye el camino desde el inicio o el objetivo hasta el nodo en común
def reconstruir_camino(camino, nodo_comun):
    camino_reconstruido = []
    nodo = nodo_comun
    while nodo is not None:
        camino_reconstruido.append(nodo)  # Añade el nodo actual al camino
        nodo = camino[nodo]  # Retrocede al nodo anterior
    return camino_reconstruido[::-1]  # Devuelve el camino en orden correcto

# Búsqueda Bidireccional
def busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo):
    if nodo_inicial == nodo_objetivo:
        return [nodo_inicial]  # Si ambos nodos son iguales, ya está el camino

    # Colas para ambas direcciones de búsqueda
    frontera_inicial = deque([nodo_inicial])
    frontera_objetivo = deque([nodo_objetivo])
    
    # Diccionarios para rastrear el camino desde cada extremo
    camino_inicial = {nodo_inicial: None}
    camino_objetivo = {nodo_objetivo: None}
    
    # Bucle principal
    while frontera_inicial and frontera_objetivo:
        # Expansión desde el nodo inicial
        nodo_actual_inicial = frontera_inicial.popleft()
        for vecino in grafo.get(nodo_actual_inicial, []):
            if vecino not in camino_inicial:
                camino_inicial[vecino] = nodo_actual_inicial  # Rastro desde el inicio
                frontera_inicial.append(vecino)

        # Expansión desde el nodo objetivo
        nodo_actual_objetivo = frontera_objetivo.popleft()
        for vecino in grafo.get(nodo_actual_objetivo, []):
            if vecino not in camino_objetivo:
                camino_objetivo[vecino] = nodo_actual_objetivo  # Rastro desde el objetivo
                frontera_objetivo.append(vecino)

        # Verificamos si hay un nodo común en ambos caminos
        nodo_comun = verificar_cruce(camino_inicial, camino_objetivo)
        if nodo_comun:
            # Unimos los dos caminos
            camino = reconstruir_camino(camino_inicial, nodo_comun) + reconstruir_camino(camino_objetivo, nodo_comun)[1:]
            return camino  # Camino final completo

    return None  # No se encontró camino
