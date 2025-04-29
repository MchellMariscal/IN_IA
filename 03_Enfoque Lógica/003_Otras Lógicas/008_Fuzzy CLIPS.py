def fuzzy_rules(temp, humedad):
    if temp >= 30:
        return "Muy caliente"
    elif temp <= 10:
        return "Muy frío"
    else:
        return "Moderado"
