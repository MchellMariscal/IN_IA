# Resolver un problema lógico con backtracking

def resolver(variables, restricciones, asignacion={}):
    if len(asignacion) == len(variables):  # Si todas las variables están asignadas
        return asignacion  # Devolvemos la asignación actual
    var = [v for v in variables if v not in asignacion][0]  # Seleccionamos una variable no asignada
    for valor in [True, False]:  # Para cada valor de verdad posible
        nueva_asignacion = asignacion.copy()  # Copiamos la asignación actual
        nueva_asignacion[var] = valor  # Asignamos un valor a la variable
        if restricciones(nueva_asignacion):  # Si la asignación cumple con las restricciones
            resultado = resolver(variables, restricciones, nueva_asignacion)  # Llamada recursiva para asignar las variables restantes
            if resultado:  # Si encontramos una solución
                return resultado  # Devolvemos la solución
    return None  # Si no hay solución

# Restricciones: p ∨ q
def restricciones(asignacion):
    if "p" in asignacion and "q" in asignacion:  # Si p y q están asignados
        return asignacion["p"] or asignacion["q"]  # Verificamos la restricción
    return True  # Si no hay restricciones violadas

resultado = resolver(["p", "q"], restricciones)  # Resolvemos el problema con backtracking
print("Solución encontrada:", resultado)  # Imprimimos la solución encontrada

# Ejemplo de aplicación real: En la resolución de problemas, el backtracking puede ser utilizado para encontrar soluciones que satisfagan restricciones lógicas, considerando la asignación de valores a variables.
