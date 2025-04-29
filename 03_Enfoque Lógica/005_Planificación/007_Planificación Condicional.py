# Plan con condición basada en sensores
def sensor_estado():
    return "sucio"  # simula lectura

plan = []
if sensor_estado() == "sucio":
    plan.append("limpiar")
else:
    plan.append("descansar")

print("Plan condicional:", plan)
