# Verificar un ejemplo de cuantificadores: ∀x (x > 0 → x² > 0)
def verificar_cuantificador():
    universo = [1, 2, 3, 4, 5]
    for x in universo:
        if x > 0 and not (x * x > 0):
            return False
    return True

print("∀x (x > 0 → x² > 0) es", verificar_cuantificador())
