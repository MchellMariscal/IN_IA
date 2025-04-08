import numpy as np

states = [0, 1, 2]
actions = [0, 1]
gamma = 0.9
theta = 0.01

# Recompensas
R = np.array([
    [5, 10],
    [-1, 2],
    [0, 0]
])

# Probabilidades de transición [estado][acción][estado siguiente]
P = [
    [[0.8, 0.2, 0.0], [0.1, 0.9, 0.0]],
    [[0.0, 0.6, 0.4], [0.0, 0.3, 0.7]],
    [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]
]

# Inicializamos la política (acción 0 para todos)
policy = [0, 0, 0]
V = np.zeros(len(states))

def policy_evaluation(policy, V):
    while True:
        delta = 0
        for s in states:
            v = V[s]
            a = policy[s]
            V[s] = sum([
                P[s][a][s_next] * (R[s][a] + gamma * V[s_next])
                for s_next in states
            ])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def policy_improvement(V, policy):
    policy_stable = True
    for s in states:
        old_action = policy[s]
        action_values = []
        for a in actions:
            q = sum([
                P[s][a][s_next] * (R[s][a] + gamma * V[s_next])
                for s_next in states
            ])
            action_values.append(q)
        best_action = np.argmax(action_values)
        policy[s] = best_action
        if best_action != old_action:
            policy_stable = False
    return policy, policy_stable

# Iteración de políticas
while True:
    V = policy_evaluation(policy, V)
    policy, stable = policy_improvement(V, policy)
    if stable:
        break

print("Valores óptimos:", V)
print("Política óptima:", policy)
