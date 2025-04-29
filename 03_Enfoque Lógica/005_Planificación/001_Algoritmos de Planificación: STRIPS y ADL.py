# Representación simple de STRIPS
initial_state = {"robot_at_A", "box_at_B"}
goal_state = {"box_at_C"}

actions = [
    {"name": "move_A_to_B", "pre": {"robot_at_A"}, "add": {"robot_at_B"}, "del": {"robot_at_A"}},
    {"name": "move_B_to_C", "pre": {"robot_at_B"}, "add": {"robot_at_C"}, "del": {"robot_at_B"}},
    {"name": "push_box", "pre": {"robot_at_B", "box_at_B"}, "add": {"box_at_C"}, "del": {"box_at_B"}},
]

def apply_action(state, action):
    if action["pre"].issubset(state):
        new_state = (state - action["del"]) | action["add"]
        return new_state
    return None

state = initial_state.copy()
plan = []

for action in actions:
    result = apply_action(state, action)
    if result:
        plan.append(action["name"])
        state = result
        if goal_state.issubset(state):
            break

print("Plan:", plan)
