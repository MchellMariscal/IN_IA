import numpy as np

# Definir el entorno Gridworld (4x4)
# 0: espacio vacío, 1: recompensa positiva, -1: recompensa negativa
grid = np.zeros((4, 4))  # Inicializamos la cuadrícula
grid[0, 3] = 1  # Meta
grid[3, 3] = -1 # Recompensa negativa

# Definir las acciones posibles
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']  # Acciones posibles
acciones_dict = {'arriba': (-1, 0), 'abajo': (1, 0), 'izquierda': (0, -1), 'derecha': (0, 1)}  # Movimientos

# Parámetros
gamma = 0.9  # Factor de descuento
epsilon = 1e-4  # Criterio de convergencia

# Inicializar V(s) y política (acciones aleatorias)
V = np.zeros((4, 4))  # Valores iniciales para cada estado
pi = np.random.choice(acciones, size=(4, 4))  # Política inicial aleatoria

# Función de evaluación de la política
def evaluar_politica(pi, V, gamma):
    delta = float('inf')  # Cambio máximo en los valores
    while delta > epsilon:  # Mientras el cambio sea mayor que el umbral
        delta = 0  # Reiniciamos el cambio máximo
        for i in range(4):  # Para cada fila
            for j in range(4):  # Para cada columna
                v = V[i, j]  # Valor actual del estado
                # Acción tomada por la política en (i, j)
                accion = pi[i, j]  # Acción según la política
                di, dj = acciones_dict[accion]  # Movimiento
                ni, nj = max(0, min(i + di, 3)), max(0, min(j + dj, 3))  # Estado siguiente
                # Recompensa
                R = grid[ni, nj]  # Recompensa del siguiente estado
                # Actualización de V(s)
                V[i, j] = R + gamma * V[ni, nj]  # Actualizamos el valor del estado
                delta = max(delta, abs(v - V[i, j]))  # Actualizamos el cambio máximo
    return V  # Devolvemos los valores

# Función de mejora de la política
def mejorar_politica(V, pi, gamma):
    policy_stable = True  # Indicador de estabilidad de la política
    for i in range(4):  # Para cada fila
        for j in range(4):  # Para cada columna
            old_action = pi[i, j]  # Acción actual según la política
            action_values = []  # Valores Q para cada acción
            for accion in acciones:  # Para cada acción
                di, dj = acciones_dict[accion]  # Movimiento
                ni, nj = max(0, min(i + di, 3)), max(0, min(j + dj, 3))  # Estado siguiente
                R = grid[ni, nj]  # Recompensa del siguiente estado
                action_value = R + gamma * V[ni, nj]  # Valor de la acción
                action_values.append(action_value)  # Añadimos el valor de la acción
            # Tomar la acción con mayor valor
            pi[i, j] = acciones[np.argmax(action_values)]  # Actualizamos la política
            if old_action != pi[i, j]:  # Si la acción cambia
                policy_stable = False  # La política no es estable
    return pi, policy_stable  # Devolvemos la política y su estabilidad

# Iteración de la política
def iteracion_politica():
    global pi, V  # Política y valores globales
    while True:  # Bucle infinito
        # Evaluar la política
        V = evaluar_politica(pi, V, gamma)  # Evaluamos la política
        # Mejorar la política
        pi, policy_stable = mejorar_politica(V, pi, gamma)  # Mejoramos la política
        if policy_stable:  # Si la política es estable
            break  # Terminamos las iteraciones
    return pi, V  # Devolvemos la política y los valores

# Ejecutar la iteración de la política
politica_optima, valores_optimos = iteracion_politica()  # Obtenemos la política y los valores óptimos

# Imprimir la política y los valores de los estados
print("Política Óptima:")  # Imprimimos la política óptima
print(politica_optima)  # Imprimimos la política
print("\nValores de los estados:")  # Imprimimos los valores de los estados
print(valores_optimos)  # Imprimimos los valores

# Ejemplo de aplicación real: En la gestión de recursos, la búsqueda de la política puede ser utilizada para determinar la mejor estrategia de asignación de recursos, maximizando la eficiencia y minimizando los costos.
