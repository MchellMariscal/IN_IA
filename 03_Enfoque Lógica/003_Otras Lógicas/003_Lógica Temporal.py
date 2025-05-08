def logica_temporal():
    estados = ['inicio', 'procesando', 'final']  # Estados del sistema
    for tiempo, estado in enumerate(estados):  # Para cada estado en el tiempo
        print(f"En t={tiempo}, el sistema está en estado: {estado}")  # Imprimimos el estado en el tiempo

# Ejemplo de aplicación real: En los sistemas de tiempo real, la lógica temporal puede ser utilizada para modelar y razonar sobre el comportamiento de sistemas a lo largo del tiempo, considerando los estados y transiciones.
