# Agente lógico sencillo: si hay obstáculo → girar
def agente_logico(percepcion):
    if percepcion == "obstaculo":
        return "girar"
    else:
        return "avanzar"

print("Acción:", agente_logico("obstaculo"))
