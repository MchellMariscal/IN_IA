from collections import defaultdict

# Relaciones de precedencia entre tareas
tasks = {
    "hacer_café": [],  # Hacer café no tiene precondiciones
    "moler_granos": [],  # Moler granos no tiene precondiciones
    "hervir_agua": ["moler_granos"],  # Hervir agua requiere moler granos
    "verter_agua": ["hervir_agua", "moler_granos"],  # Verter agua requiere hervir agua y moler granos
    "beber": ["hacer_café", "verter_agua"]  # Beber requiere hacer café y verter agua
}

# Función para ordenar tareas topológicamente
def topological_sort(tasks):
    visited = set()  # Conjunto de tareas visitadas
    order = []  # Orden de las tareas

    def visit(task):
        if task not in visited:  # Si la tarea no ha sido visitada
            visited.add(task)  # Marcamos la tarea como visitada
            for pre in tasks[task]:  # Para cada precondición de la tarea
                visit(pre)  # Llamada recursiva para visitar la precondición
            order.append(task)  # Añadimos la tarea al orden

    for t in tasks:  # Para cada tarea
        visit(t)  # Visitamos la tarea
    return list(reversed(order))  # Devolvemos el orden en orden inverso

print("Orden parcial:", topological_sort(tasks))  # Imprimimos el orden parcial

# Ejemplo de aplicación real: En la gestión de proyectos, la planificación de orden parcial puede ser utilizada para ordenar tareas basadas en sus dependencias, considerando las precondiciones y efectos.
