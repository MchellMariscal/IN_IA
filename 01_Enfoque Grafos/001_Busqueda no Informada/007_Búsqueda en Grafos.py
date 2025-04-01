def dfs_camino(grafo, nodo_inicial, nodo_objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    
    visitados.add(nodo_inicial)
    camino.append(nodo_inicial)
    
    if nodo_inicial == nodo_objetivo:
        return camino
    
    for vecino in grafo.get(nodo_inicial, []):
        if vecino not in visitados:
            resultado = dfs_camino(grafo, vecino, nodo_objetivo, visitados, camino)
            if resultado:
                return resultado
    
    camino.pop()  # Retroceder si no encontramos el objetivo
    return None

# Prueba de DFS para encontrar un camino
camino_dfs = dfs_camino(grafo, 'A', 'G')
print(f'Camino encontrado con DFS: {camino_dfs}')
