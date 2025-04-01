# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Mapa con regiones y sus vecinos
mapa = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Función para verificar si una asignación de colores es válida
def es_valida(asignacion, region, color):
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Algoritmo CSP con Backtracking
def csp_colorear(asignacion, regiones):
    if not regiones:  # Si todas las regiones están coloreadas, terminamos
        return asignacion
    
    region = regiones.pop(0)  # Seleccionamos una región
    for color in colores:
        if es_valida(asignacion, region, color):  # Verificamos restricciones
            asignacion[region] = color
            resultado = csp_colorear(asignacion, regiones.copy())  # Llamada recursiva
            if resultado:
                return resultado
            asignacion.pop(region)  # Deshacemos la asignación si no funciona
    
    return None  # Si no hay solución

# Ejecutamos el CSP
solucion = csp_colorear({}, list(mapa.keys()))
print(f'Solución encontrada: {solucion}')
