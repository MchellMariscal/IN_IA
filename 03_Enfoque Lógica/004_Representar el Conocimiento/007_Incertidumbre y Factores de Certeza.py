def diagnosticar(sintomas):
    # Definimos enfermedades con sus síntomas y factores de certeza
    enfermedades = {
        "gripe": ({"fiebre", "tos"}, 0.85),  # Gripe con síntomas y factor de certeza
        "alergia": ({"estornudos", "ojos_rojos"}, 0.65)  # Alergia con síntomas y factor de certeza
    }

    for enfermedad, (requisitos, certeza) in enfermedades.items():  # Para cada enfermedad
        if requisitos.issubset(sintomas):  # Si los síntomas son un subconjunto de los síntomas del paciente
            return f"{enfermedad} con certeza de {certeza * 100}%"  # Devolvemos el diagnóstico con certeza
    return "Sin diagnóstico concluyente"  # Si no hay diagnóstico concluyente

print(diagnosticar({"fiebre", "tos"}))  # Imprimimos el diagnóstico para síntomas de gripe

# Ejemplo de aplicación real: En los sistemas de diagnóstico, los factores de certeza pueden ser utilizados para manejar la incertidumbre en el diagnóstico, considerando los síntomas y su relación con enfermedades.
