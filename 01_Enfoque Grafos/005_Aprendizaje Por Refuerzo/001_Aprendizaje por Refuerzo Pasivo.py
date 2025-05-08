import numpy as np
import random

# Configuración del entorno: una cuadrícula 2x4
grid = [
    [0, 0, 0, +1],  # Fila 0: recompensas
    [0, None, 0, -1] # Fila 1: None representa un estado no accesible
]

# Política fija: siempre ir a la derecha
acciones = {'→': (0, 1)}

# Parámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento

# Valores iniciales: inicializamos los valores de los estados accesibles a 0
V = {}
for i in range(2):  # Para cada fila
    for j in range(4):  # Para cada columna
        if grid[i][j] is not None:  # Si el estado es accesible
            V[(i, j)] = 0.0  # Inicializamos el valor del estado

# Función para seguir la política fija
def paso_estado(s):
    i, j = s  # Estado actual
    di, dj = acciones['→']  # Dirección de la acción
    nuevo_i, nuevo_j = i + di, j + dj  # Nuevo estado
    # Verificamos si el nuevo estado es válido
    if 0 <= nuevo_i < 2 and 0 <= nuevo_j < 4 and grid[nuevo_i][nuevo_j] is not None:
        return (nuevo_i, nuevo_j)  # Devolvemos el nuevo estado
    return (i, j)  # Si no es válido, permanecemos en el mismo estado

# Entrenamiento: simular episodios
episodios = 1000
for _ in range(episodios):  # Para cada episodio
    estado = (0, 0)  # Estado inicial
    while estado not in [(0, 3), (1, 3)]:  # Estados terminales
        siguiente = paso_estado(estado)  # Obtenemos el siguiente estado
        recompensa = grid[siguiente[0]][siguiente[1]]  # Obtenemos la recompensa
        # Actualizamos el valor del estado actual
        V[estado] += alpha * (recompensa + gamma * V[siguiente] - V[estado])
        estado = siguiente  # Actualizamos el estado

# Mostrar valores estimados
print("Valores estimados de los estados:")
for i in range(2):  # Para cada fila
    fila = ""  # Cadena para la fila
    for j in range(4):  # Para cada columna
        if grid[i][j] is None:  # Si el estado no es accesible
            fila += "#####  "  # Representamos el estado no accesible
        else:
            fila += f"{V[(i,j)]:.2f}  "  # Representamos el valor del estado
    print(fila)  # Imprimimos la fila

# Ejemplo de aplicación real: En la optimización de rutas de transporte, el aprendizaje por refuerzo pasivo puede ser utilizado para evaluar rutas fijas, mejorando la eficiencia de las rutas existentes sin cambiar la política.
