# HTN simple: Tarea "limpiar casa" compuesta por sub-tareas
htn = {
    "limpiar_casa": ["barrer", "trapear", "sacar_basura"]
}

def planificar_htn(tarea):
    if tarea in htn:
        return [planificar_htn(sub) for sub in htn[tarea]]
    else:
        return tarea

print("Plan jerárquico:", planificar_htn("limpiar_casa"))
