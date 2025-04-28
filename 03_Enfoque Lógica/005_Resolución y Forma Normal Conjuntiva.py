# Convertir (p → q) en Forma Normal Conjuntiva
def forma_normal_conjuntiva(p, q):
    return (not p) or q

# Ejemplo
p, q = True, False
resultado = forma_normal_conjuntiva(p, q)
print("Resultado de (¬p ∨ q):", resultado)
