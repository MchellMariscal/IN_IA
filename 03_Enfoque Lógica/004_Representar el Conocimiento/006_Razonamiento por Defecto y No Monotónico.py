def puede_volar(animal):
    # Definimos excepciones al razonamiento por defecto
    excepciones = ["pingüino", "avestruz"]  # Excepciones
    if animal in excepciones:  # Si el animal es una excepción
        return f"{animal} NO puede volar."  # Devolvemos que no puede volar
    return f"{animal} probablemente puede volar."  # Devolvemos que probablemente puede volar

print(puede_volar("águila"))  # Imprimimos el resultado para un águila
print(puede_volar("pingüino"))  # Imprimimos el resultado para un pingüino

# Ejemplo de aplicación real: En el razonamiento por defecto, las excepciones pueden ser utilizadas para manejar información incompleta o incierta, considerando reglas generales y excepciones.
