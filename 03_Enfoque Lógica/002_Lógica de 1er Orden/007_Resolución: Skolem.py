# Skolemización: eliminar cuantificadores existenciales
# Ejemplo: ∃x P(x) → P(Skolem)

def skolemizar(formula):
    if "∃" in formula:  # Si la fórmula contiene un cuantificador existencial
        return formula.replace("∃x", "SkolemFunc()")  # Reemplazamos el cuantificador existencial con una función de Skolem
    return formula  # Devolvemos la fórmula sin cambios

formula = "∃x Amigo(x, Juan)"  # Fórmula con cuantificador existencial
print("Después de Skolemización:", skolemizar(formula))  # Imprimimos el resultado de la skolemización

# Ejemplo de aplicación real: En la lógica de primer orden, la skolemización puede ser utilizada para eliminar cuantificadores existenciales en fórmulas, considerando la introducción de funciones de Skolem.
