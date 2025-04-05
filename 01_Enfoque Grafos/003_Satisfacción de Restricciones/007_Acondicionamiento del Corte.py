import itertools

# Colores posibles
colores = ['Rojo', 'Verde', 'Azul']

# Grafo cíclico
grafo = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'A']
}

# Corte para romper el ciclo
cutset = ['A']

# Función para verificar conflictos
def es_valido(asignacion, nodo, color):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Resolución del subproblema (como árbol)
def resolver_sin_ciclos(asignacion):
    nodos_restantes = [n for n in grafo if n not in asignacion]
    if not nodos_restantes:
        return asignacion

    nodo = nodos_restantes[0]
    for color in colores:
        if es_valido(asignacion, nodo, color):
            asignacion[nodo] = color
            resultado = resolver_sin_ciclos(asignacion.copy())
            if resultado:
                return resultado
            del asignacion[nodo]
    return None

# Probamos todas las combinaciones posibles del cutset
for combinacion in itertools.product(colores, repeat=len(cutset)):
    asignacion = dict(zip(cutset, combinacion))
    if all(es_valido(asignacion, nodo, color) for nodo, color in asignacion.items()):
        resultado = resolver_sin_ciclos(asignacion.copy())
        if resultado:
            print("✅ Solución encontrada:", resultado)
            break
else:
    print("❌ No se encontró solución.")