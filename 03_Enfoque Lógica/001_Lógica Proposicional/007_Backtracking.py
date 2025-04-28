# Resolver un problema lógico con backtracking

def resolver(variables, restricciones, asignacion={}):
    if len(asignacion) == len(variables):
        return asignacion
    var = [v for v in variables if v not in asignacion][0]
    for valor in [True, False]:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[var] = valor
        if restricciones(nueva_asignacion):
            resultado = resolver(variables, restricciones, nueva_asignacion)
            if resultado:
                return resultado
    return None

# Restricciones: p ∨ q
def restricciones(asignacion):
    if "p" in asignacion and "q" in asignacion:
        return asignacion["p"] or asignacion["q"]
    return True

resultado = resolver(["p", "q"], restricciones)
print("Solución encontrada:", resultado)
