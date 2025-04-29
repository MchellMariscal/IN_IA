def inferencia_difusa(temperatura, humedad):
    if temperatura > 25 and humedad < 50:
        return "Encender aire acondicionado"
    elif temperatura < 15:
        return "Encender calefacción"
    else:
        return "Mantener ambiente"
