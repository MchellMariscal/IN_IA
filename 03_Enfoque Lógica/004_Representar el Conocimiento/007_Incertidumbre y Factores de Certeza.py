def diagnosticar(sintomas):
    enfermedades = {
        "gripe": ({"fiebre", "tos"}, 0.85),
        "alergia": ({"estornudos", "ojos_rojos"}, 0.65)
    }

    for enfermedad, (requisitos, certeza) in enfermedades.items():
        if requisitos.issubset(sintomas):
            return f"{enfermedad} con certeza de {certeza * 100}%"
    return "Sin diagnóstico concluyente"

print(diagnosticar({"fiebre", "tos"}))
