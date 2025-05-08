# Simulación básica con dos agentes
agentes = {
    "robot1": ["cargar", "transportar"],  # Acciones del robot1
    "robot2": ["esperar", "recibir"]  # Acciones del robot2
}

for agente, acciones in agentes.items():  # Para cada agente
    print(f"Agente {agente}:")  # Imprimimos el nombre del agente
    for a in acciones:  # Para cada acción del agente
        print(f"  - {a}")  # Imprimimos la acción

# Ejemplo de aplicación real: En los sistemas multiagente, la planificación continua puede ser utilizada para coordinar acciones entre múltiples agentes, considerando las acciones y objetivos de cada agente.
