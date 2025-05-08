# Función para verificar si es seguro colocar una reina en la posición (fila, col)
def es_valida(tablero, fila, col):
    for i in range(fila):  # Para cada fila anterior
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):  # Si hay otra reina en la misma columna o en las diagonales
            return False  # No es seguro colocar la reina
    return True  # Es seguro colocar la reina

# Función de backtracking para resolver el problema de las N-Reinas
def backtracking_n_reinas(tablero, fila, n):
    if fila == n:  # Si todas las reinas están colocadas, hemos encontrado una solución
        return [list(tablero)]  # Guardamos una copia de la solución

    soluciones = []  # Lista para guardar las soluciones
    for col in range(n):  # Probamos colocar una reina en cada columna de la fila actual
        if es_valida(tablero, fila, col):  # Si es seguro colocar la reina
            tablero[fila] = col  # Colocamos la reina en la posición (fila, col)
            soluciones += backtracking_n_reinas(tablero, fila + 1, n)  # Llamada recursiva para colocar las reinas restantes
            tablero[fila] = -1  # Quitamos la reina (backtrack) para probar otras posiciones

    return soluciones  # Devolvemos las soluciones encontradas

# Función para resolver el problema de las N-Reinas
def resolver_n_reinas(n):
    tablero = [-1] * n  # Inicializamos un tablero vacío con -1
    soluciones = backtracking_n_reinas(tablero, 0, n)  # Buscamos todas las soluciones posibles
    return soluciones  # Devolvemos las soluciones encontradas

# Ejecutamos la búsqueda para N = 4
soluciones = resolver_n_reinas(4)
for i, sol in enumerate(soluciones):
    print(f"Solución {i + 1}: {sol}")

# Ejemplo de aplicación real: En la planificación de rutas de entrega, la búsqueda de vuelta atrás puede ser utilizada para encontrar rutas que cumplan con múltiples restricciones, como tiempos de entrega y capacidades de los vehículos.
