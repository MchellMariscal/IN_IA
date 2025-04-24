
# Grafo representado como diccionario de adyacencia dirigido
# Las claves son nodos y los valores son listas de nodos hijos (a los que apunta)
graph = {
    'A': ['X'],     # A es padre de X
    'C': ['X'],     # C es padre de X
    'X': ['Y'],     # X es padre de Y
    'B': ['Y']      # B también es padre de Y
}

# Función para encontrar el Manto de Markov de un nodo
def manto_de_markov(grafo, nodo):
    # Encontrar los padres: nodos que apuntan a 'nodo'
    padres = [n for n, hijos in grafo.items() if nodo in hijos]
    
    # Encontrar los hijos: nodos a los que 'nodo' apunta
    hijos = grafo.get(nodo, [])

    # Encontrar los otros padres de los hijos (sin incluir al nodo mismo)
    padres_de_hijos = []
    for hijo in hijos:
        padres_de_hijos.extend([n for n, hs in grafo.items() if hijo in hs and n != nodo])

    # Unir padres, hijos y padres de hijos (sin duplicados)
    manto = set(padres + hijos + padres_de_hijos)
    return manto

# Ejemplo de uso
nodo = 'X'
manto = manto_de_markov(graph, nodo)
print(f"El Manto de Markov del nodo '{nodo}' es: {manto}")

# Salida esperada:
# El Manto de Markov del nodo 'X' es: {'A', 'C', 'Y', 'B'}
