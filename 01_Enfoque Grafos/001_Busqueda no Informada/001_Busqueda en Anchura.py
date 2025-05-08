from collections import deque  # Importamos deque para usarlo como cola eficiente

def bfs(graph, start):
    visited = set()  # Conjunto para registrar los nodos que ya hemos visitado
    queue = deque([start])  # Inicializamos la cola con el nodo de inicio
    resultado = []  # Lista para guardar el orden de los nodos visitados

    # Mientras haya nodos por explorar
    while queue:
        node = queue.popleft()  # Sacamos el nodo que está al frente de la cola (FIFO)
        
        if node not in visited:  # Si no lo hemos visitado aún
            visited.add(node)  # Lo marcamos como visitado
            resultado.append(node)  # Lo agregamos al resultado (orden de visita)
            
            # Agregamos sus vecinos a la cola para ser visitados más adelante
            queue.extend(graph[node])
    
    return resultado  # Retornamos la lista con el recorrido BFS
