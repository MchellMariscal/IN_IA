import itertools

# Colores posibles para colorear el grafo
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

# Función para verificar conflictos al asignar un color a un nodo
def es_valido(asignacion, nodo, color):
    for vecino in grafo[nodo]:  # Para cada vecino del nodo
        if vecino in asignacion and asignacion[vecino] == color:  # Si el vecino ya tiene el mismo color
            return False  # La asignación no es válida
    return True  # La asignación es válida

# Resolución del subproblema (como árbol) sin ciclos
def resolver_sin_ciclos(asignacion):
    nodos_restantes = [n for n in grafo if n not in asignacion]  # Nodos restantes por colorear
    if not nodos_restantes:  # Si no hay nodos restantes
        return asignacion  # Devolvemos la asignación actual

    nodo = nodos_restantes[0]  # Seleccionamos un nodo para colorear
    for color in colores:  # Probamos cada color posible
        if es_valido(asignacion, nodo, color):  # Si el color cumple con las restricciones
            asignacion[nodo] = color  # Asignamos el color al nodo
            resultado = resolver_sin_ciclos(asignacion.copy())  # Llamada recursiva para colorear los nodos restantes
            if resultado:  # Si encontramos una solución
                return resultado  # Devolvemos la solución
            del asignacion[nodo]  # Deshacemos la asignación si no lleva a una solución
    return None  # Si no hay solución

# Probamos todas las combinaciones posibles del cutset
for combinacion in itertools.product(colores, repeat=len(cutset)):  # Para cada combinación de colores del cutset
    asignacion = dict(zip(cutset, combinacion))  # Asignamos los colores del cutset
    if all(es_valido(asignacion, nodo, color) for nodo, color in asignacion.items()):  # Si la asignación cumple con las restricciones
        resultado = resolver_sin_ciclos(asignacion.copy())  # Llamada recursiva para colorear los nodos restantes
        if resultado:  # Si encontramos una solución
            print("✅ Solución encontrada:", resultado)  # Imprimimos la solución
            break  # Terminamos el bucle
else:
    print("❌ No se encontró solución.")  # Si no hay solución

# Ejemplo de aplicación real: En la planificación de redes de distribución, el acondicionamiento del corte puede ser utilizado para dividir una red compleja en subredes más manejables, facilitando la optimización de rutas y recursos.
