def es_valida(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def backtracking_n_reinas(tablero, fila, n):
    if fila == n:
        return [list(tablero)]  # Guardamos una copia de la solución
    
    soluciones = []
    for col in range(n):
        if es_valida(tablero, fila, col):
            tablero[fila] = col  # Colocamos la reina
            soluciones += backtracking_n_reinas(tablero, fila + 1, n)
            tablero[fila] = -1  # Quitamos la reina (backtrack)
    
    return soluciones

def resolver_n_reinas(n):
    tablero = [-1] * n  # Inicializamos un tablero vacío
    soluciones = backtracking_n_reinas(tablero, 0, n)
    return soluciones

# Ejecutamos la búsqueda para N = 4
soluciones = resolver_n_reinas(4)
for i, sol in enumerate(soluciones):
    print(f"Solución {i + 1}: {sol}")
