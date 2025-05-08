# Base de conocimiento sencilla como lista de proposiciones
base_conocimiento = [
    "P → Q",  # Proposición 1
    "Q → R",  # Proposición 2
    "P"        # Proposición 3
]

print("Base de Conocimiento:")  # Imprimimos el encabezado
for regla in base_conocimiento:  # Para cada regla en la base de conocimiento
    print(regla)  # Imprimimos la regla

# Ejemplo de aplicación real: En los sistemas de inteligencia artificial, una base de conocimiento puede ser utilizada para almacenar reglas y hechos, permitiendo la inferencia de nueva información.
