# Representación simple de STRIPS
initial_state = {"robot_at_A", "box_at_B"}  # Estado inicial
goal_state = {"box_at_C"}  # Estado objetivo

# Definición de acciones posibles
actions = [
    {"name": "move_A_to_B", "pre": {"robot_at_A"}, "add": {"robot_at_B"}, "del": {"robot_at_A"}},  # Acción: mover de A a B
    {"name": "move_B_to_C", "pre": {"robot_at_B"}, "add": {"robot_at_C"}, "del": {"robot_at_B"}},  # Acción: mover de B a C
    {"name": "push_box", "pre": {"robot_at_B", "box_at_B"}, "add": {"box_at_C"}, "del": {"box_at_B"}},  # Acción: empujar la caja
]

# Función para aplicar una acción al estado actual
def apply_action(state, action):
    if action["pre"].issubset(state):  # Si las precondiciones se cumplen
        new_state = (state - action["del"]) | action["add"]  # Aplicamos los efectos de la acción
        return new_state
    return None  # Si no se puede aplicar la acción

state = initial_state.copy()  # Copiamos el estado inicial
plan = []  # Inicializamos el plan

for action in actions:  # Para cada acción
    result = apply_action(state, action)  # Aplicamos la acción
    if result:  # Si la acción se puede aplicar
        plan.append(action["name"])  # Añadimos la acción al plan
        state = result  # Actualizamos el estado
        if goal_state.issubset(state):  # Si el estado objetivo se alcanza
            break  # Terminamos el plan

print("Plan:", plan)  # Imprimimos el plan

# Ejemplo de aplicación real: En la robótica, los algoritmos de planificación como STRIPS pueden ser utilizados para planificar rutas y acciones de robots, considerando los estados iniciales y objetivos.
