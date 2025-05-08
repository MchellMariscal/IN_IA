# Unificación simple de predicados
def unificar(pred1, pred2):
    if pred1.split("(")[0] == pred2.split("(")[0]:  # Si los predicados tienen el mismo nombre
        return "Unificación exitosa"  # Los predicados se pueden unificar
    else:
        return "No se puede unificar"  # Los predicados no se pueden unificar

print(unificar("padre(juan, maria)", "padre(X, maria)"))  # Imprimimos el resultado de la unificación

# Ejemplo de aplicación real: En la lógica de primer orden, la unificación puede ser utilizada para encontrar sustituciones que hagan que dos expresiones lógicas sean idénticas, considerando los términos y variables.
