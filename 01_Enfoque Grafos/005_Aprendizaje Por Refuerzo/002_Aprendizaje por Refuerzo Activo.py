import numpy as np
import random

# Definir el entorno (Gridworld 4x4)
grid = np.zeros((4, 4))
grid[0, 3] = 1  # Recompensa en la posición (0, 3)
grid[3, 3] = -1 # Recompensa negativa en (3, 3)

# Configuración del entorno
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']

# Parámetros
alpha = 0.1  # tasa de aprendizaje
gamma = 0.9  # factor de descuento
epsilon = 0.1  # tasa de exploración

# Inicializar Q con ceros
Q = np.zeros((4, 4, len(acciones)))

# Función de movimiento: mapea el estado actual y la acción a un nuevo estado
def siguiente_estado(state, action):
    i, j = state
    if action == 'arriba' and i > 0:
        return (i - 1, j)
    if action == 'abajo' and i < 3:
        return (i + 1, j)
    if action == 'izquierda' and j > 0:
        return (i, j - 1)
    if action == 'derecha' and j < 3:
        return (i, j + 1)
    return state  # Si no se puede mover, permanece en el mismo estado

# Función para seleccionar la acción (exploración/explotación)
def seleccionar_accion(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(acciones)  # Exploración
    else:
        i, j = state
        return acciones[np.argmax(Q[i, j])]  # Explotación

# Entrenamiento del agente con Q-learning
episodios = 1000
for _ in range(episodios):
    estado = (3, 0)  # Comienza en la esquina inferior izquierda
    while estado != (0, 3):  # El objetivo es (0, 3)
        accion = seleccionar_accion(estado)
        siguiente = siguiente_estado(estado, accion)
        recompensa = grid[siguiente]  # Recompensa basada en el siguiente estado
        i, j = estado
        a = acciones.index(accion)
        siguiente_i, siguiente_j = siguiente
        # Actualizar Q con la fórmula de Bellman
        Q[i, j, a] += alpha * (recompensa + gamma * np.max(Q[siguiente_i, siguiente_j]) - Q[i, j, a])
        estado = siguiente

# Ver los valores finales de Q
print("Valores finales de Q (estado, acción):")
for i in range(4):
    for j in range(4):
        print(f"Estado ({i},{j}): {Q[i,j]}")
