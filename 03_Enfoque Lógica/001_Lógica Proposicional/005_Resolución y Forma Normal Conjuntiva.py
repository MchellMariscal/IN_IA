# Convertir (p → q) en Forma Normal Conjuntiva
def forma_normal_conjuntiva(p, q):
    return (not p) or q  # La implicación lógica es equivalente a ¬p ∨ q

# Ejemplo
p, q = True, False  # Valores de verdad de p y q
resultado = forma_normal_conjuntiva(p, q)  # Convertimos la implicación a forma normal conjuntiva
print("Resultado de (¬p ∨ q):", resultado)  # Imprimimos el resultado

# Ejemplo de aplicación real: En la lógica proposicional, la forma normal conjuntiva puede ser utilizada para estandarizar expresiones lógicas, facilitando la aplicación de algoritmos de resolución.
