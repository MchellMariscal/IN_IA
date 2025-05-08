# Colores disponibles para colorear el mapa
colores = ['Rojo', 'Verde', 'Azul']

# Mapa con regiones y sus vecinos. Cada región tiene una lista de regiones adyacentes.
mapa = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Función para verificar si una asignación de colores es válida
# Comprueba si el color asignado a una región es diferente al de sus vecinos.
def es_valida(asignacion, region, color):
    for vecino in mapa[region]:  # Para cada vecino de la región
        if vecino in asignacion and asignacion[vecino] == color:  # Si el vecino ya tiene el mismo color
            return False  # La asignación no es válida
    return True  # La asignación es válida

# Algoritmo CSP con Backtracking para colorear el mapa
def csp_colorear(asignacion, regiones):
    if not regiones:  # Si no hay más regiones por colorear, hemos encontrado una solución
        return asignacion  # Devolvemos la asignación actual

    region = regiones.pop(0)  # Seleccionamos una región para colorear
    for color in colores:  # Probamos cada color posible
        if es_valida(asignacion, region, color):  # Verificamos si el color cumple con las restricciones
            asignacion[region] = color  # Asignamos el color a la región
            resultado = csp_colorear(asignacion, regiones.copy())  # Llamada recursiva para colorear las regiones restantes
            if resultado:  # Si encontramos una solución
                return resultado  # Devolvemos la solución
            asignacion.pop(region)  # Deshacemos la asignación si no lleva a una solución

    return None  # Si no hay solución

# Ejecutamos el CSP para encontrar una solución de coloración
solucion = csp_colorear({}, list(mapa.keys()))
print(f'Solución encontrada: {solucion}')

# Ejemplo de aplicación real: En la planificación de horarios escolares, un CSP puede ser utilizado para asignar aulas y horarios a diferentes clases, asegurando que no haya conflictos de horarios o aulas.
