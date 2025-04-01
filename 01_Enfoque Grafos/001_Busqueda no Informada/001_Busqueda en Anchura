# Búsqueda en Anchura (BFS)
# Implementación en Python

from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para nodos visitados
    queue = deque([start])  # Cola para la exploración
    resultado = []  # Lista para almacenar el recorrido

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            resultado.append(node)
            queue.extend(graph[node])  # Agregar nodos adyacentes a la cola
    
    return resultado

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

inicio = 'A'
recorrido = bfs(graph, inicio)
print("Recorrido BFS desde", inicio, ":", recorrido)
