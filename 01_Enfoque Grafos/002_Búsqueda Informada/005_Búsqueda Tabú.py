import random

# Grafo de ejemplo con valores heurísticos asociados a cada nodo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Heurística asociada a cada nodo (a mayor valor, mejor estado)
heuristica = {
    'A': 1,
    'B': 3,
    'C': 5,
    'D': 7,
    'E': 4,
    'F': 6,
    'G': 8  # Nodo con mejor heurística (óptimo global)
}

def busqueda_tabu(grafo, nodo_inicial, iteraciones_max, tamaño_tabu):
    estado_actual = nodo_inicial
    mejor_estado = estado_actual
    lista_tabu = []
    
    for _ in range(iteraciones_max):
        vecinos = grafo.get(estado_actual, [])
        
        # Filtrar los vecinos que están en la lista tabú
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]
        
        if not vecinos_validos:  # Si no hay opciones disponibles, terminamos
            break
        
        # Elegir el mejor vecino basado en la heurística
        mejor_vecino = max(vecinos_validos, key=lambda v: heuristica[v])
        
        # Actualizar el estado actual
        estado_actual = mejor_vecino
        
        # Guardar el mejor estado encontrado
        if heuristica[estado_actual] > heuristica[mejor_estado]:
            mejor_estado = estado_actual
        
        # Agregar el estado actual a la lista tabú
        lista_tabu.append(estado_actual)
        
        # Limitar el tamaño de la lista tabú
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)
    
    return mejor_estado

# Ejecutar la Búsqueda Tabú desde 'A'
mejor_estado_encontrado = busqueda_tabu(grafo, 'A', iteraciones_max=10, tamaño_tabu=3)
print(f'Mejor estado encontrado con Búsqueda Tabú: {mejor_estado_encontrado}')
