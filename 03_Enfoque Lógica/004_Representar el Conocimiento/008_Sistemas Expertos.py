def sistema_experto(respuestas):
    # Definimos reglas para un sistema experto simple
    if respuestas["dolor"] == "cabeza" and respuestas["visión_borrosa"]:  # Si hay dolor de cabeza y visión borrosa
        return "Podría ser migraña"  # Devolvemos un posible diagnóstico
    elif respuestas["dolor"] == "estómago" and respuestas["náuseas"]:  # Si hay dolor de estómago y náuseas
        return "Posible gastritis"  # Devolvemos otro posible diagnóstico
    return "Consulta con un médico"  # Si no hay diagnóstico concluyente

res = {"dolor": "estómago", "náuseas": True, "visión_borrosa": False}  # Respuestas del paciente
print(sistema_experto(res))  # Imprimimos el diagnóstico del sistema experto

# Ejemplo de aplicación real: En los sistemas expertos, las reglas pueden ser utilizadas para realizar diagnósticos basados en respuestas a preguntas, considerando las reglas y hechos conocidos.
