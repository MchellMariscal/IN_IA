# Skolemización: eliminar cuantificadores existenciales
# Ejemplo: ∃x P(x) → P(Skolem)

def skolemizar(formula):
    if "∃" in formula:
        return formula.replace("∃x", "SkolemFunc()")
    return formula

formula = "∃x Amigo(x, Juan)"
print("Después de Skolemización:", skolemizar(formula))
