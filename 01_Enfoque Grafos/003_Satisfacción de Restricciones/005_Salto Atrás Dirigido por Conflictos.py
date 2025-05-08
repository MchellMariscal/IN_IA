# Función para verificar si es válido asignar un color a un nodo
def es_valido(asignacion, grafo, nodo, color):
    for vecino in grafo[nodo]:  # Para cada vecino del nodo
        if vecino in asignacion and asignacion[vecino] == color:  # Si el vecino ya tiene el mismo color
            return False  # La asignación no es válida
    return True  # La asignación es válida

# Función de salto atrás dirigido por conflictos para colorear un grafo
def salto_atras_conflictos(nodos, grafo, colores, asignacion, index, conflicto):
    if index == len(nodos):  # Si todos los nodos están coloreados, hemos encontrado una solución
        return asignacion  # Devolvemos la asignación actual

    nodo = nodos[index]  # Seleccionamos un nodo para colorear
    for color in colores:  # Probamos cada color posible
        if es_valido(asignacion, grafo, nodo, color):  # Si el color cumple con las restricciones
            asignacion[nodo] = color  # Asignamos el color al nodo
            resultado = salto_atras_conflictos(nodos, grafo, colores, asignacion, index + 1, conflicto)  # Llamada recursiva para colorear los nodos restantes
            if resultado:  # Si encontramos una solución
                return resultado  # Devolvemos la solución
            del asignacion[nodo]  # Deshacemos la asignación si no lleva a una solución
        else:
            conflicto[nodo] = conflicto.get(nodo, set())  # Obtenemos los conflictos del nodo
            for vecino in grafo[nodo]:  # Para cada vecino del nodo
                if asignacion.get(vecino) == color:  # Si el vecino tiene el mismo color
                    conflicto[nodo].add(vecino)  # Añadimos el vecino a los conflictos del nodo

    # Salto hacia el último nodo con conflicto
    if nodo in conflicto:  # Si el nodo tiene conflictos
        conflictos_previos = [nodos.index(c) for c in conflicto[nodo] if c in nodos[:index]]  # Obtenemos los índices de los nodos con conflictos previos
        if conflictos_previos:  # Si hay nodos con conflictos previos
            salto = max(conflictos_previos)  # Obtenemos el índice del último nodo con conflicto
            return salto_atras_conflictos(nodos, grafo, colores, asignacion, salto, conflicto)  # Llamada recursiva para colorear los nodos restantes

    return None  # Si no hay solución

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

# Ejemplo de aplicación real: En la asignación de frecuencias en redes de telecomunicaciones, el salto atrás dirigido por conflictos puede ser utilizado para asignar frecuencias a estaciones de manera que no haya interferencias.
