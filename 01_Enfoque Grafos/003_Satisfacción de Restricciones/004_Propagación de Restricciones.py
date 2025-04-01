from collections import deque

# Función para encontrar las casillas vacías en el Sudoku
def encontrar_vacias(tablero):
    vacias = []
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                vacias.append((fila, col))
    return vacias

# Función para obtener los valores posibles en una casilla
def obtener_dominio(tablero, fila, col):
    numeros = set(range(1, 10))
    
    # Eliminar números de la misma fila y columna
    numeros -= set(tablero[fila])
    numeros -= {tablero[f][col] for f in range(9)}
    
    # Eliminar números del subcuadrante 3x3
    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            numeros.discard(tablero[inicio_fila + i][inicio_col + j])

    return list(numeros)

# Algoritmo AC-3 para hacer la propagación de restricciones
def ac3(tablero):
    cola = deque()
    
    # Agregar todas las casillas vacías a la cola
    vacias = encontrar_vacias(tablero)
    for casilla in vacias:
        cola.append(casilla)
    
    while cola:
        fila, col = cola.popleft()
        dominio = obtener_dominio(tablero, fila, col)
        
        if len(dominio) == 1:
            tablero[fila][col] = dominio[0]  # Asignar valor único
            
            # Volver a verificar restricciones para vecinos
            for i in range(9):
                if tablero[fila][i] == 0:
                    cola.append((fila, i))
                if tablero[i][col] == 0:
                    cola.append((i, col))
            
            inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if tablero[inicio_fila + i][inicio_col + j] == 0:
                        cola.append((inicio_fila + i, inicio_col + j))

    return tablero

# Tablero de Sudoku con casillas vacías representadas por 0
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Aplicamos la propagación de restricciones con AC-3
solucion = ac3(sudoku)

# Imprimimos el Sudoku parcialmente resuelto
for fila in solucion:
    print(fila)
