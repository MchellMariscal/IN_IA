# DFS para encontrar un camino de un nodo a otro, no solo recorrer
def dfs_camino(grafo, nodo_inicial, nodo_objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()  # Inicializamos conjunto de nodos visitados
    if camino is None:
        camino = []  # Inicializamos lista de camino

    visitados.add(nodo_inicial)  # Marcamos el nodo como visitado
    camino.append(nodo_inicial)  # Lo agregamos al camino actual

    if nodo_inicial == nodo_objetivo:
        return camino  # Si encontramos el objetivo, retornamos el camino

    for vecino in grafo.get(nodo_inicial, []):  # Recorremos sus vecinos
        if vecino not in visitados:
            resultado = dfs_camino(grafo, vecino, nodo_objetivo, visitados, camino)  # Llamada recursiva
            if resultado:
                return resultado  # Si encontramos el camino, lo devolvemos

    camino.pop()  # Retrocedemos (backtracking) si no lleva al objetivo
    return None  # No se encontró el objetivo desde este camino
