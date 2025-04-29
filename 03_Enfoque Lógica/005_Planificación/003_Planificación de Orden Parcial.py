# Relaciones de precedencia entre tareas
from collections import defaultdict

tasks = {
    "hacer_café": [],
    "moler_granos": [],
    "hervir_agua": ["moler_granos"],
    "verter_agua": ["hervir_agua", "moler_granos"],
    "beber": ["hacer_café", "verter_agua"]
}

def topological_sort(tasks):
    visited = set()
    order = []

    def visit(task):
        if task not in visited:
            visited.add(task)
            for pre in tasks[task]:
                visit(pre)
            order.append(task)

    for t in tasks:
        visit(t)
    return list(reversed(order))

print("Orden parcial:", topological_sort(tasks))
