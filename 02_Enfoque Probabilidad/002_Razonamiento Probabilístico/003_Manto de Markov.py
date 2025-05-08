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
    padres = [n for n, hijos in grafo.items() if nodo in hijos]  # Nodos que tienen a 'nodo' como hijo

    # Encontrar los hijos: nodos a los que 'nodo' apunta
    hijos = grafo.get(nodo, [])  # Nodos a los que 'nodo' apunta

    # Encontrar los otros padres de los hijos (sin incluir al nodo mismo)
    padres_de_hijos = []  # Lista para los padres de los hijos
    for hijo in hijos:  # Para cada hijo
        padres_de_hijos.extend([n for n, hs in grafo.items() if hijo in hs and n != nodo])  # Nodos que tienen al hijo como hijo y no son el nodo

    # Unir padres, hijos y padres de hijos (sin duplicados)
    manto = set(padres + hijos + padres_de_hijos)  # Conjunto de nodos en el manto de Markov
    return manto  # Devolvemos el manto de Markov

# Ejemplo de uso
nodo = 'X'
manto = manto_de_markov(graph, nodo)  # Calculamos el manto de Markov para el nodo 'X'
print(f"El Manto de Markov del nodo '{nodo}' es: {manto}")  # Imprimimos el manto de Markov

# Salida esperada:
# El Manto de Markov del nodo 'X' es: {'A', 'C', 'Y', 'B'}

# Ejemplo de aplicación real: En el análisis de redes sociales, el manto de Markov puede ser utilizado para identificar los nodos más influyentes en una red, considerando las conexiones directas e indirectas.
