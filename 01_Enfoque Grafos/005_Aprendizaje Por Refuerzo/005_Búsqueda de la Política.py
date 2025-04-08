import numpy as np

# Definir el entorno Gridworld (4x4)
# 0: espacio vacío, 1: recompensa positiva, -1: recompensa negativa
grid = np.zeros((4, 4))
grid[0, 3] = 1  # Meta
grid[3, 3] = -1 # Recompensa negativa

# Definir las acciones posibles
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']
acciones_dict = {'arriba': (-1, 0), 'abajo': (1, 0), 'izquierda': (0, -1), 'derecha': (0, 1)}

# Parámetros
gamma = 0.9  # factor de descuento
epsilon = 1e-4  # criterio de convergencia

# Inicializar V(s) y política (acciones aleatorias)
V = np.zeros((4, 4))  # Valor de cada estado
pi = np.random.choice(acciones, size=(4, 4))  # Política inicial aleatoria

# Función de evaluación de la política
def evaluar_politica(pi, V, gamma):
    delta = float('inf')
    while delta > epsilon:
        delta = 0
        for i in range(4):
            for j in range(4):
                v = V[i, j]
                # Acción tomada por la política en (i, j)
                accion = pi[i, j]
                di, dj = acciones_dict[accion]
                ni, nj = max(0, min(i + di, 3)), max(0, min(j + dj, 3))  # Estado siguiente
                # Recompensa
                R = grid[ni, nj]
                # Actualización de V(s)
                V[i, j] = R + gamma * V[ni, nj]
                delta = max(delta, abs(v - V[i, j]))
    return V

# Función de mejora de la política
def mejorar_politica(V, pi, gamma):
    policy_stable = True
    for i in range(4):
        for j in range(4):
            old_action = pi[i, j]
            action_values = []
            for accion in acciones:
                di, dj = acciones_dict[accion]
                ni, nj = max(0, min(i + di, 3)), max(0, min(j + dj, 3))
                R = grid[ni, nj]
                action_value = R + gamma * V[ni, nj]
                action_values.append(action_value)
            # Tomar la acción con mayor valor
            pi[i, j] = acciones[np.argmax(action_values)]
            if old_action != pi[i, j]:
                policy_stable = False
    return pi, policy_stable

# Iteración de la política
def iteracion_politica():
    global pi, V
    while True:
        # Evaluar la política
        V = evaluar_politica(pi, V, gamma)
        # Mejorar la política
        pi, policy_stable = mejorar_politica(V, pi, gamma)
        if policy_stable:
            break
    return pi, V

# Ejecutar la iteración de la política
politica_optima, valores_optimos = iteracion_politica()

# Imprimir la política y los valores de los estados
print("Política Óptima:")
print(politica_optima)
print("\nValores de los estados:")
print(valores_optimos)
