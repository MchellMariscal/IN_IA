def es_valida(asignacion, fila, col):
    for i in range(fila):
        if asignacion[i] == col or abs(asignacion[i] - col) == abs(i - fila):
            return False
    return True

def forward_checking(asignacion, dominios, fila, n):
    if fila == n:
        return [list(asignacion)]  # Guardamos una solución
    
    soluciones = []
    for col in dominios[fila]:  # Solo probamos valores viables
        if es_valida(asignacion, fila, col):
            asignacion[fila] = col
            
            # Reducimos dominios para la siguiente fila
            nuevos_dominios = [list(dom) for dom in dominios]
            for i in range(fila + 1, n):
                if col in nuevos_dominios[i]:
                    nuevos_dominios[i].remove(col)
                diagonal1 = col + (i - fila)
                diagonal2 = col - (i - fila)
                if diagonal1 in nuevos_dominios[i]:
                    nuevos_dominios[i].remove(diagonal1)
                if diagonal2 in nuevos_dominios[i]:
                    nuevos_dominios[i].remove(diagonal2)

            # Si todas las filas aún tienen valores posibles, continuamos
            if all(nuevos_dominios[i] for i in range(fila + 1, n)):
                soluciones += forward_checking(asignacion, nuevos_dominios, fila + 1, n)
            
            asignacion[fila] = -1  # Deshacer asignación

    return soluciones

def resolver_n_reinas_fc(n):
    asignacion = [-1] * n  # Tablero vacío
    dominios = [list(range(n)) for _ in range(n)]  # Todos los valores posibles
    soluciones = forward_checking(asignacion, dominios, 0, n)
    return soluciones

# Ejecutamos la búsqueda con Forward Checking para N = 4
soluciones = resolver_n_reinas_fc(4)
for i, sol in enumerate(soluciones):
    print(f"Solución {i + 1}: {sol}")
