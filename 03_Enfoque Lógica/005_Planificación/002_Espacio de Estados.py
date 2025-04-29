# Grafo simple de estados (representado como diccionario)
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

def dfs(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath: return newpath
    return None

print("Ruta:", dfs(graph, "A", "E"))
