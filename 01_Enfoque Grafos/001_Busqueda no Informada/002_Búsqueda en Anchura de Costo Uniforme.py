import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]  # (costo, nodo)
    visited = {}  # Almacena el costo mínimo para llegar a cada nodo
    path = {}  # Para reconstruir el camino
    
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if node in visited and cost >= visited[node]:
            continue
        
        visited[node] = cost
        
        if node == goal:
            break
        
        for neighbor, weight in graph.get(node, []):
            heapq.heappush(priority_queue, (cost + weight, neighbor))
            path[neighbor] = node
    
    return visited, path

# Ejemplo de uso
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('H', 2)],
    'F': [('C', 3), ('G', 6)],
    'G': [('F', 6)],
    'H': [('E', 2)]
}

start = 'A'
goal = 'H'
visited, path = uniform_cost_search(graph, start, goal)
print("Costo mínimo para cada nodo:", visited)
print("Camino más corto:", path)
