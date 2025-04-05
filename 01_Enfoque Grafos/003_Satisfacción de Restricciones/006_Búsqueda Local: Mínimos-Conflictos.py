import random

def contar_conflictos(tablero, fila, col):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        if i == fila:
            continue
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            conflictos += 1
    return conflictos

def encontrar_columna_min_conflictos(tablero, fila):
    n = len(tablero)
    min_conflictos = float('inf')
    mejores_columnas = []
    
    for col in range(n):
        conflictos = contar_conflictos(tablero, fila, col)
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            mejores_columnas = [col]
        elif conflictos == min_conflictos:
            mejores_columnas.append(col)
    
    return random.choice(mejores_columnas)

def min_conflicts(n, max_iter=1000):
    # Generar una solución inicial aleatoria
    tablero = [random.randint(0, n-1) for _ in range(n)]

    for _ in range(max_iter):
        # Buscar filas en conflicto
        conflictos = [fila for fila in range(n) if contar_conflictos(tablero, fila, tablero[fila]) > 0]
        
        if not conflictos:
            return tablero  # ¡Solución encontrada!

        fila = random.choice(conflictos)
        tablero[fila] = encontrar_columna_min_conflictos(tablero, fila)

    return None  # No se encontró solución

# Ejecutamos el algoritmo
n = 8
solucion = min_conflicts(n)

# Mostramos el resultado
if solucion:
    print(f"Solución encontrada para {n}-Reinas:")
    for fila in range(n):
        print(" ".join("Q" if solucion[fila] == col else "." for col in range(n)))
else:
    print("No se encontró solución.")