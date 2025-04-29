# Simulación básica con dos agentes
agentes = {
    "robot1": ["cargar", "transportar"],
    "robot2": ["esperar", "recibir"]
}

for agente, acciones in agentes.items():
    print(f"Agente {agente}:")
    for a in acciones:
        print(f"  - {a}")
