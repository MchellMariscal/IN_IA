# Verificar un ejemplo de cuantificadores: ∀x (x > 0 → x² > 0)
def verificar_cuantificador():
    universo = [1, 2, 3, 4, 5]  # Definimos un universo de valores
    for x in universo:  # Para cada valor en el universo
        if x > 0 and not (x * x > 0):  # Si x es mayor que 0 y x² no es mayor que 0
            return False  # La proposición no es verdadera para todos los valores
    return True  # La proposición es verdadera para todos los valores

print("∀x (x > 0 → x² > 0) es", verificar_cuantificador())  # Imprimimos el resultado

# Ejemplo de aplicación real: En la lógica de primer orden, los cuantificadores pueden ser utilizados para evaluar proposiciones sobre un universo de valores, considerando la validez de las proposiciones para todos los elementos.
