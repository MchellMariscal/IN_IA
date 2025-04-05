def es_valido(asignacion, grafo, nodo, color):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def salto_atras_conflictos(nodos, grafo, colores, asignacion, index, conflicto):
    if index == len(nodos):
        return asignacion

    nodo = nodos[index]
    for color in colores:
        if es_valido(asignacion, grafo, nodo, color):
            asignacion[nodo] = color
            resultado = salto_atras_conflictos(nodos, grafo, colores, asignacion, index + 1, conflicto)
            if resultado:
                return resultado
            del asignacion[nodo]
        else:
            conflicto[nodo] = conflicto.get(nodo, set())
            for vecino in grafo[nodo]:
                if asignacion.get(vecino) == color:
                    conflicto[nodo].add(vecino)

    # Salto hacia el último nodo con conflicto
    if nodo in conflicto:
        conflictos_previos = [nodos.index(c) for c in conflicto[nodo] if c in nodos[:index]]
        if conflictos_previos:
            salto = max(conflictos_previos)
            return salto_atras_conflictos(nodos, grafo, colores, asignacion, salto, conflicto)

    return None

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colores = ['Rojo', 'Verde', 'Azul']
nodos = list(grafo.keys())
asignacion = {}
conflicto = {}

solucion = salto_atras_conflictos(nodos, grafo, colores, asignacion, 0, conflicto)
print("Asignación encontrada:", solucion)
