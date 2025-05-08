import random

# Grafo con vecinos para cada nodo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Heurística (valor de cada nodo, donde mayor es mejor)
heuristica = {
    'A': 1,
    'B': 3,
    'C': 5,
    'D': 7,
    'E': 4,
    'F': 6,
    'G': 8  # Nodo óptimo
}

def busqueda_haz_local(grafo, nodos_iniciales, k, iteraciones_max):
    estados_actuales = nodos_iniciales  # k estados iniciales

    for _ in range(iteraciones_max):
        vecinos = []

        # Generamos vecinos de los estados actuales
        for estado in estados_actuales:
            vecinos.extend(grafo.get(estado, []))

        # Seleccionamos los k mejores estados según la heurística
        estados_actuales = sorted(set(vecinos), key=lambda x: heuristica[x], reverse=True)[:k]

        # Si alguno de los estados es el mejor posible, terminamos
        if 'G' in estados_actuales:
            return 'G'

    return estados_actuales[0]  # Devolvemos el mejor estado encontrado

# Ejecutamos la Búsqueda de Haz Local con k=2 y 10 iteraciones
mejor_estado = busqueda_haz_local(grafo, ['A', 'C'], k=2, iteraciones_max=10)
print(f'Mejor estado encontrado con Búsqueda de Haz Local: {mejor_estado}')

# Ejemplo de aplicación real: En la planificación de proyectos, la búsqueda de haz local puede ser utilizada para seleccionar las mejores tareas a realizar en cada etapa del proyecto, optimizando el uso de recursos y el tiempo de finalización.
