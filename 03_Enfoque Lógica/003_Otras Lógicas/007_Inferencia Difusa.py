def inferencia_difusa(temperatura, humedad):
    if temperatura > 25 and humedad < 50:  # Si la temperatura es alta y la humedad es baja
        return "Encender aire acondicionado"  # Encendemos el aire acondicionado
    elif temperatura < 15:  # Si la temperatura es baja
        return "Encender calefacción"  # Encendemos la calefacción
    else:  # En otros casos
        return "Mantener ambiente"  # Mantenemos el ambiente

# Ejemplo de aplicación real: En los sistemas de control de clima, la inferencia difusa puede ser utilizada para tomar decisiones basadas en condiciones ambientales, considerando reglas difusas para determinar acciones.
