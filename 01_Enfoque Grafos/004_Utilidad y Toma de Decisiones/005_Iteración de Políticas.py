import numpy as np

states = [0, 1, 2]  # Estados
actions = [0, 1]  # Acciones
gamma = 0.9  # Factor de descuento
theta = 0.01  # Umbral de convergencia

# Recompensas
R = np.array([
    [5, 10],  # recompensas en el estado 0
    [-1, 2],  # estado 1
    [0, 0]    # estado 2 (terminal)
])

# Probabilidades de transición [estado][acción][estado siguiente]
P = [
    [[0.8, 0.2, 0.0], [0.1, 0.9, 0.0]],  # desde estado 0, acción 0 y 1
    [[0.0, 0.6, 0.4], [0.0, 0.3, 0.7]],  # desde estado 1
    [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]   # estado 2, no cambia
]

# Inicializamos la política (acción 0 para todos)
policy = [0, 0, 0]  # Política inicial
V = np.zeros(len(states))  # Valores iniciales para cada estado

def policy_evaluation(policy, V):
    while True:
        delta = 0  # Cambio máximo en los valores
        for s in states:  # Para cada estado
            v = V[s]  # Valor actual del estado
            a = policy[s]  # Acción según la política
            V[s] = sum([
                P[s][a][s_next] * (R[s][a] + gamma * V[s_next])  # Cálculo del valor del estado
                for s_next in states  # Para cada estado siguiente
            ])
            delta = max(delta, abs(v - V[s]))  # Actualizamos el cambio máximo
        if delta < theta:  # Si el cambio es menor que el umbral
            break  # Terminamos la evaluación
    return V  # Devolvemos los valores

def policy_improvement(V, policy):
    policy_stable = True  # Indicador de estabilidad de la política
    for s in states:  # Para cada estado
        old_action = policy[s]  # Acción actual según la política
        action_values = []  # Valores Q para cada acción
        for a in actions:  # Para cada acción
            q = sum([
                P[s][a][s_next] * (R[s][a] + gamma * V[s_next])  # Cálculo del valor Q
                for s_next in states  # Para cada estado siguiente
            ])
            action_values.append(q)  # Añadimos el valor Q
        best_action = np.argmax(action_values)  # Mejor acción
        policy[s] = best_action  # Actualizamos la política
        if best_action != old_action:  # Si la acción cambia
            policy_stable = False  # La política no es estable
    return policy, policy_stable  # Devolvemos la política y su estabilidad

# Iteración de políticas
while True:
    V = policy_evaluation(policy, V)  # Evaluamos la política
    policy, stable = policy_improvement(V, policy)  # Mejoramos la política
    if stable:  # Si la política es estable
        break  # Terminamos las iteraciones

print("Valores óptimos:", V)  # Imprimimos los valores óptimos
print("Política óptima:", policy)  # Imprimimos la política óptima

# Ejemplo de aplicación real: En la gestión de inventarios, la iteración de políticas puede ser utilizada para determinar la mejor estrategia de reabastecimiento, considerando las demandas y costos asociados.
