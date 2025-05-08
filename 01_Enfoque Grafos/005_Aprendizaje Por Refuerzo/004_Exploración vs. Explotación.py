import numpy as np
import random

# Definir el entorno (Gridworld 4x4)
grid = np.zeros((4, 4))  # Inicializamos la cuadrícula
grid[0, 3] = 1  # Recompensa en la posición (0, 3)
grid[3, 3] = -1 # Recompensa negativa en (3, 3)

# Configuración del entorno
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']  # Acciones posibles

# Parámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Tasa de exploración

# Inicializar Q con ceros
Q = np.zeros((4, 4, len(acciones)))  # Valores Q iniciales

# Función de movimiento: mapea el estado actual y la acción a un nuevo estado
def siguiente_estado(state, action):
    i, j = state  # Estado actual
    if action == 'arriba' and i > 0:  # Mover arriba
        return (i - 1, j)  # Nuevo estado
    if action == 'abajo' and i < 3:  # Mover abajo
        return (i + 1, j)  # Nuevo estado
    if action == 'izquierda' and j > 0:  # Mover izquierda
        return (i, j - 1)  # Nuevo estado
    if action == 'derecha' and j < 3:  # Mover derecha
        return (i, j + 1)  # Nuevo estado
    return state  # Si no se puede mover, permanece en el mismo estado

# Función para seleccionar la acción (exploración/explotación)
def seleccionar_accion(state, epsilon):
    if random.uniform(0, 1) < epsilon:  # Exploración
        return random.choice(acciones)  # Acción aleatoria
    else:  # Explotación
        i, j = state  # Estado actual
        return acciones[np.argmax(Q[i, j])]  # Acción con mayor valor Q

# Entrenamiento del agente con Q-learning
episodios = 1000
for _ in range(episodios):  # Para cada episodio
    estado = (3, 0)  # Comienza en la esquina inferior izquierda
    while estado != (0, 3):  # El objetivo es (0, 3)
        accion = seleccionar_accion(estado, epsilon)  # Seleccionamos una acción
        siguiente = siguiente_estado(estado, accion)  # Obtenemos el siguiente estado
        recompensa = grid[siguiente]  # Obtenemos la recompensa
        i, j = estado  # Estado actual
        a = acciones.index(accion)  # Índice de la acción
        siguiente_i, siguiente_j = siguiente  # Siguiente estado
        # Actualizar Q con la fórmula de Bellman
        Q[i, j, a] += alpha * (recompensa + gamma * np.max(Q[siguiente_i, siguiente_j]) - Q[i, j, a])
        estado = siguiente  # Actualizamos el estado

# Ver los valores finales de Q
print("Valores finales de Q (estado, acción):")
for i in range(4):  # Para cada fila
    for j in range(4):  # Para cada columna
        print(f"Estado ({i},{j}): {Q[i,j]}")  # Imprimimos los valores Q

# Ejemplo de aplicación real: En la publicidad en línea, la exploración vs. explotación puede ser utilizada para decidir si mostrar nuevos anuncios (exploración) o los más efectivos conocidos (explotación), maximizando los clics y conversiones.
