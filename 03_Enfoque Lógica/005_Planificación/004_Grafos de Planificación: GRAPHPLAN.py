# Fase de expansión de GRAPHPLAN simplificada
levels = [{"at_room1", "clean"}, {"move_to_room2"}, {"at_room2"}]

def graphplan_search(goal, levels):
    plan = []
    for level in reversed(levels):
        if goal in level:
            plan.append(goal)
    return plan[::-1]

print("Plan GRAPHPLAN:", graphplan_search("at_room2", levels))
