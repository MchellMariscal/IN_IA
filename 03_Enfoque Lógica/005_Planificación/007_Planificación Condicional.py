# Plan con condición basada en sensores
def sensor_estado():
    return "sucio"  # Simula lectura de un sensor

plan = []  # Inicializamos el plan
if sensor_estado() == "sucio":  # Si el sensor indica que está sucio
    plan.append("limpiar")  # Añadimos "limpiar" al plan
else:
    plan.append("descansar")  # Añadimos "descansar" al plan

print("Plan condicional:", plan)  # Imprimimos el plan condicional

# Ejemplo de aplicación real: En la robótica, la planificación condicional puede ser utilizada para tomar decisiones basadas en lecturas de sensores, considerando las condiciones del entorno.
