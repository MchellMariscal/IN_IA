# Agente lógico sencillo: si hay obstáculo → girar
def agente_logico(percepcion):
    if percepcion == "obstaculo":  # Si la percepción es un obstáculo
        return "girar"  # Girar para evitar el obstáculo
    else:
        return "avanzar"  # Avanzar si no hay obstáculo

print("Acción:", agente_logico("obstaculo"))  # Imprimimos la acción del agente

# Ejemplo de aplicación real: En la robótica, los agentes lógicos pueden ser utilizados para tomar decisiones basadas en percepciones del entorno, considerando reglas lógicas para determinar acciones.
