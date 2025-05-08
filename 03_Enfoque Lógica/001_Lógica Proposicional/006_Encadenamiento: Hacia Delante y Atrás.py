# Encadenamiento hacia adelante (Forward chaining)

# Base de conocimiento
hechos = {"P"}  # Hechos conocidos
reglas = {"P → Q", "Q → R"}  # Reglas de inferencia

# Encadenamiento
def encadenamiento_hacia_adelante(hechos, reglas):
    nuevos = set()  # Conjunto para nuevos hechos inferidos
    for regla in reglas:  # Para cada regla
        antecedente, consecuente = regla.split(" → ")  # Dividimos la regla en antecedente y consecuente
        if antecedente in hechos:  # Si el antecedente es un hecho conocido
            nuevos.add(consecuente)  # Añadimos el consecuente a los nuevos hechos
    return hechos.union(nuevos)  # Devolvemos la unión de los hechos conocidos y los nuevos hechos

nuevos_hechos = encadenamiento_hacia_adelante(hechos, reglas)  # Aplicamos el encadenamiento hacia adelante
print("Hechos después del encadenamiento:", nuevos_hechos)  # Imprimimos los hechos después del encadenamiento

# Ejemplo de aplicación real: En los sistemas expertos, el encadenamiento hacia adelante puede ser utilizado para inferir nuevos hechos a partir de reglas y hechos conocidos, considerando la aplicación de reglas de inferencia.
