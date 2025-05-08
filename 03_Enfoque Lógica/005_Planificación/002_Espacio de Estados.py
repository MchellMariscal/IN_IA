# Grafo simple de estados (representado como diccionario)
graph = {
    "A": ["B", "C"],  # Desde A se puede ir a B y C
    "B": ["D"],       # Desde B se puede ir a D
    "C": ["D"],       # Desde C se puede ir a D
    "D": ["E"],       # Desde D se puede ir a E
    "E": []           # E es un estado terminal
}

# Función de búsqueda en profundidad (DFS)
def dfs(graph, start, goal, path=[]):
    path = path + [start]  # Añadimos el estado actual al camino
    if start == goal:  # Si el estado actual es el objetivo
        return path  # Devolvemos el camino
    for node in graph[start]:  # Para cada estado vecino
        if node not in path:  # Si el estado vecino no está en el camino
            newpath = dfs(graph, node, goal, path)  # Llamada recursiva para explorar el estado vecino
            if newpath: return newpath  # Si se encuentra el objetivo, devolvemos el camino
    return None  # Si no se encuentra el objetivo

print("Ruta:", dfs(graph, "A", "E"))  # Imprimimos la ruta encontrada

# Ejemplo de aplicación real: En la inteligencia artificial, la búsqueda en el espacio de estados puede ser utilizada para encontrar rutas en problemas de planificación, considerando los estados y transiciones posibles.
