# Función para verificar si es seguro colocar una reina en la posición (fila, col)
def es_valida(asignacion, fila, col):
    for i in range(fila):  # Para cada fila anterior
        if asignacion[i] == col or abs(asignacion[i] - col) == abs(i - fila):  # Si hay otra reina en la misma columna o en las diagonales
            return False  # No es seguro colocar la reina
    return True  # Es seguro colocar la reina

# Función de forward checking para resolver el problema de las N-Reinas
def forward_checking(asignacion, dominios, fila, n):
    if fila == n:  # Si todas las reinas están colocadas, hemos encontrado una solución
        return [list(asignacion)]  # Guardamos una solución

    soluciones = []  # Lista para guardar las soluciones
    for col in dominios[fila]:  # Solo probamos valores viables
        if es_valida(asignacion, fila, col):  # Si es seguro colocar la reina
            asignacion[fila] = col  # Colocamos la reina en la posición (fila, col)

            # Reducimos dominios para la siguiente fila
            nuevos_dominios = [list(dom) for dom in dominios]  # Copiamos los dominios actuales
            for i in range(fila + 1, n):  # Para cada fila siguiente
                if col in nuevos_dominios[i]:  # Si el valor está en el dominio de la fila
                    nuevos_dominios[i].remove(col)  # Eliminamos el valor del dominio
                diagonal1 = col + (i - fila)  # Diagonal hacia abajo a la derecha
                diagonal2 = col - (i - fila)  # Diagonal hacia abajo a la izquierda
                if diagonal1 in nuevos_dominios[i]:  # Si el valor está en el dominio de la fila
                    nuevos_dominios[i].remove(diagonal1)  # Eliminamos el valor del dominio
                if diagonal2 in nuevos_dominios[i]:  # Si el valor está en el dominio de la fila
                    nuevos_dominios[i].remove(diagonal2)  # Eliminamos el valor del dominio

            # Si todas las filas aún tienen valores posibles, continuamos
            if all(nuevos_dominios[i] for i in range(fila + 1, n)):  # Si todas las filas tienen valores posibles
                soluciones += forward_checking(asignacion, nuevos_dominios, fila + 1, n)  # Llamada recursiva para colocar las reinas restantes

            asignacion[fila] = -1  # Deshacer asignación

    return soluciones  # Devolvemos las soluciones encontradas

# Función para resolver el problema de las N-Reinas con forward checking
def resolver_n_reinas_fc(n):
    asignacion = [-1] * n  # Tablero vacío
    dominios = [list(range(n)) for _ in range(n)]  # Todos los valores posibles
    soluciones = forward_checking(asignacion, dominios, 0, n)  # Buscamos todas las soluciones posibles
    return soluciones  # Devolvemos las soluciones encontradas

# Ejecutamos la búsqueda con Forward Checking para N = 4
soluciones = resolver_n_reinas_fc(4)
for i, sol in enumerate(soluciones):
    print(f"Solución {i + 1}: {sol}")

# Ejemplo de aplicación real: En la asignación de recursos en proyectos, la comprobación hacia adelante puede ser utilizada para asignar recursos a tareas, asegurando que no se excedan las capacidades disponibles.
