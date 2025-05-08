def fuzzy_rules(temp, humedad):
    if temp >= 30:  # Si la temperatura es muy alta
        return "Muy caliente"  # Devolvemos "Muy caliente"
    elif temp <= 10:  # Si la temperatura es muy baja
        return "Muy frío"  # Devolvemos "Muy frío"
    else:  # En otros casos
        return "Moderado"  # Devolvemos "Moderado"

# Ejemplo de aplicación real: En los sistemas de control difuso, las reglas difusas pueden ser utilizadas para modelar y razonar sobre condiciones ambientales, considerando la lógica difusa para determinar acciones.
