from collections import deque

# Función para encontrar las casillas vacías en el Sudoku
def encontrar_vacias(tablero):
    vacias = []  # Lista para guardar las casillas vacías
    for fila in range(9):  # Para cada fila
        for col in range(9):  # Para cada columna
            if tablero[fila][col] == 0:  # Si la casilla está vacía
                vacias.append((fila, col))  # Añadimos la casilla a la lista
    return vacias  # Devolvemos la lista de casillas vacías

# Función para obtener los valores posibles en una casilla
def obtener_dominio(tablero, fila, col):
    numeros = set(range(1, 10))  # Todos los números posibles

    # Eliminar números de la misma fila y columna
    numeros -= set(tablero[fila])  # Eliminamos los números de la misma fila
    numeros -= {tablero[f][col] for f in range(9)}  # Eliminamos los números de la misma columna

    # Eliminar números del subcuadrante 3x3
    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3  # Calculamos el inicio del subcuadrante
    for i in range(3):  # Para cada fila del subcuadrante
        for j in range(3):  # Para cada columna del subcuadrante
            numeros.discard(tablero[inicio_fila + i][inicio_col + j])  # Eliminamos los números del subcuadrante

    return list(numeros)  # Devolvemos los números posibles

# Algoritmo AC-3 para hacer la propagación de restricciones
def ac3(tablero):
    cola = deque()  # Cola para guardar las casillas a revisar

    # Agregar todas las casillas vacías a la cola
    vacias = encontrar_vacias(tablero)  # Obtenemos las casillas vacías
    for casilla in vacias:  # Para cada casilla vacía
        cola.append(casilla)  # Añadimos la casilla a la cola

    while cola:  # Mientras haya casillas en la cola
        fila, col = cola.popleft()  # Obtenemos la primera casilla de la cola
        dominio = obtener_dominio(tablero, fila, col)  # Obtenemos los valores posibles para la casilla

        if len(dominio) == 1:  # Si solo hay un valor posible
            tablero[fila][col] = dominio[0]  # Asignamos el valor a la casilla

            # Volver a verificar restricciones para vecinos
            for i in range(9):  # Para cada fila
                if tablero[fila][i] == 0:  # Si la casilla está vacía
                    cola.append((fila, i))  # Añadimos la casilla a la cola
                if tablero[i][col] == 0:  # Si la casilla está vacía
                    cola.append((i, col))  # Añadimos la casilla a la cola

            inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3  # Calculamos el inicio del subcuadrante
            for i in range(3):  # Para cada fila del subcuadrante
                for j in range(3):  # Para cada columna del subcuadrante
                    if tablero[inicio_fila + i][inicio_col + j] == 0:  # Si la casilla está vacía
                        cola.append((inicio_fila + i, inicio_col + j))  # Añadimos la casilla a la cola

    return tablero  # Devolvemos el tablero con las casillas asignadas

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

# Ejemplo de aplicación real: En la resolución de puzzles como el Sudoku, la propagación de restricciones puede ser utilizada para reducir el espacio de búsqueda y encontrar soluciones más rápidamente.
