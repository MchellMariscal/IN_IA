import random

# Función para contar los conflictos de una reina en una posición dada
def contar_conflictos(tablero, fila, col):
    conflictos = 0  # Contador de conflictos
    n = len(tablero)  # Tamaño del tablero
    for i in range(n):  # Para cada fila
        if i == fila:  # Si es la misma fila
            continue  # Saltamos a la siguiente iteración
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):  # Si hay otra reina en la misma columna o en las diagonales
            conflictos += 1  # Incrementamos el contador de conflictos
    return conflictos  # Devolvemos el número de conflictos

# Función para encontrar la columna con el mínimo número de conflictos para una fila dada
def encontrar_columna_min_conflictos(tablero, fila):
    n = len(tablero)  # Tamaño del tablero
    min_conflictos = float('inf')  # Inicializamos el mínimo número de conflictos
    mejores_columnas = []  # Lista para guardar las columnas con el mínimo número de conflictos

    for col in range(n):  # Para cada columna
        conflictos = contar_conflictos(tablero, fila, col)  # Contamos los conflictos de la reina en la posición (fila, col)
        if conflictos < min_conflictos:  # Si el número de conflictos es menor que el mínimo
            min_conflictos = conflictos  # Actualizamos el mínimo número de conflictos
            mejores_columnas = [col]  # Actualizamos la lista de columnas con el mínimo número de conflictos
        elif conflictos == min_conflictos:  # Si el número de conflictos es igual al mínimo
            mejores_columnas.append(col)  # Añadimos la columna a la lista de columnas con el mínimo número de conflictos

    return random.choice(mejores_columnas)  # Devolvemos una columna aleatoria de la lista de columnas con el mínimo número de conflictos

# Algoritmo de mínimos-conflictos para resolver el problema de las N-Reinas
def min_conflicts(n, max_iter=1000):
    tablero = [random.randint(0, n-1) for _ in range(n)]  # Generamos una solución inicial aleatoria

    for _ in range(max_iter):  # Para cada iteración
        conflictos = [fila for fila in range(n) if contar_conflictos(tablero, fila, tablero[fila]) > 0]  # Buscamos filas en conflicto

        if not conflictos:  # Si no hay filas en conflicto
            return tablero  # ¡Solución encontrada!

        fila = random.choice(conflictos)  # Seleccionamos una fila en conflicto aleatoriamente
        tablero[fila] = encontrar_columna_min_conflictos(tablero, fila)  # Movemos la reina a la columna con el mínimo número de conflictos

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

# Ejemplo de aplicación real: En la optimización de horarios de trabajo, la búsqueda local de mínimos-conflictos puede ser utilizada para asignar turnos a empleados, minimizando los conflictos de horarios y preferencias.
