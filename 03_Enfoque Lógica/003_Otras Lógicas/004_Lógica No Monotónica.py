def no_monotonica():
    conocimiento = {"llueve": True}  # Conocimiento inicial
    print("Inicial:", conocimiento)  # Imprimimos el conocimiento inicial
    conocimiento["llueve"] = False  # Actualizamos el conocimiento
    print("Actualizado:", conocimiento)  # Imprimimos el conocimiento actualizado

# Ejemplo de aplicación real: En los sistemas de revisión de creencias, la lógica no monotónica puede ser utilizada para manejar información que cambia con el tiempo, considerando la revisión de creencias previas.
