# Fase de expansión de GRAPHPLAN simplificada
levels = [{"at_room1", "clean"}, {"move_to_room2"}, {"at_room2"}]  # Niveles de estados

# Función para buscar un plan en GRAPHPLAN
def graphplan_search(goal, levels):
    plan = []  # Inicializamos el plan
    for level in reversed(levels):  # Para cada nivel en orden inverso
        if goal in level:  # Si el objetivo está en el nivel
            plan.append(goal)  # Añadimos el objetivo al plan
    return plan[::-1]  # Devolvemos el plan en orden inverso

print("Plan GRAPHPLAN:", graphplan_search("at_room2", levels))  # Imprimimos el plan

# Ejemplo de aplicación real: En la planificación automatizada, GRAPHPLAN puede ser utilizado para encontrar planes en problemas complejos, considerando los niveles de estados y acciones.
