def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()  # Inicializamos conjunto de visitados
    
    visited.add(start)  # Visitamos el nodo actual
    print(start, end=' ')  # Mostramos el nodo
    
    for neighbor in graph.get(start, []):  # Recorremos sus vecinos
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)  # Llamada recursiva
