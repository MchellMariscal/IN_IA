# HTN simple: Tarea "limpiar casa" compuesta por sub-tareas
htn = {
    "limpiar_casa": ["barrer", "trapear", "sacar_basura"]  # Tarea "limpiar casa" compuesta por sub-tareas
}

# Función para planificar una tarea jerárquica
def planificar_htn(tarea):
    if tarea in htn:  # Si la tarea tiene sub-tareas
        return [planificar_htn(sub) for sub in htn[tarea]]  # Planificamos las sub-tareas
    else:
        return tarea  # Devolvemos la tarea

print("Plan jerárquico:", planificar_htn("limpiar_casa"))  # Imprimimos el plan jerárquico

# Ejemplo de aplicación real: En la gestión de tareas, las redes jerárquicas de tareas pueden ser utilizadas para descomponer tareas complejas en sub-tareas más simples, considerando la estructura jerárquica.
