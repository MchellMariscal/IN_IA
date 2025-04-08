import numpy as np
import random

# Configuración del entorno
grid = [
    [0, 0, 0, +1],
    [0, None, 0, -1]
]

acciones = {'→': (0, 1)}  # política fija: siempre ir a la derecha

# Parámetros
alpha = 0.1  # tasa de aprendizaje
gamma = 0.9  # factor de descuento

# Valores iniciales
V = {}
for i in range(2):
    for j in range(4):
        if grid[i][j] is not None:
            V[(i, j)] = 0.0

# Función para seguir la política fija
def paso_estado(s):
    i, j = s
    di, dj = acciones['→']
    nuevo_i, nuevo_j = i + di, j + dj
    if 0 <= nuevo_i < 2 and 0 <= nuevo_j < 4 and grid[nuevo_i][nuevo_j] is not None:
        return (nuevo_i, nuevo_j)
    return (i, j)

# Entrenamiento: simular episodios
episodios = 1000
for _ in range(episodios):
    estado = (0, 0)
    while estado not in [(0, 3), (1, 3)]:  # estados terminales
        siguiente = paso_estado(estado)
        recompensa = grid[siguiente[0]][siguiente[1]]
        V[estado] += alpha * (recompensa + gamma * V[siguiente] - V[estado])
        estado = siguiente

# Mostrar valores estimados
print("Valores estimados de los estados:")
for i in range(2):
    fila = ""
    for j in range(4):
        if grid[i][j] is None:
            fila += "#####  "
        else:
            fila += f"{V[(i,j)]:.2f}  "
    print(fila)
