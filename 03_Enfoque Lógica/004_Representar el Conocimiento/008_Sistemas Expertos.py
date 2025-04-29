def sistema_experto(respuestas):
    if respuestas["dolor"] == "cabeza" and respuestas["visión_borrosa"]:
        return "Podría ser migraña"
    elif respuestas["dolor"] == "estómago" and respuestas["náuseas"]:
        return "Posible gastritis"
    return "Consulta con un médico"

res = {"dolor": "estómago", "náuseas": True, "visión_borrosa": False}
print(sistema_experto(res))
