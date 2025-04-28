# Encadenamiento hacia adelante (Forward chaining)

# Base de conocimiento
hechos = {"P"}
reglas = {"P → Q", "Q → R"}

# Encadenamiento
def encadenamiento_hacia_adelante(hechos, reglas):
    nuevos = set()
    for regla in reglas:
        antecedente, consecuente = regla.split(" → ")
        if antecedente in hechos:
            nuevos.add(consecuente)
    return hechos.union(nuevos)

nuevos_hechos = encadenamiento_hacia_adelante(hechos, reglas)
print("Hechos después del encadenamiento:", nuevos_hechos)
